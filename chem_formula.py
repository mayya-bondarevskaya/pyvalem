# -*- coding: utf-8 -*-
# chem_formula.py
# Version 1.0b
# A class representing a chemical formula, ChemFormula, and methods for
# parsing ChemFormula objects into existence from text strings.
#
# Copyright (C) 2012 Christian Hill
# Department of Physics and Astronomy, University College London
# christian.hill@ucl.ac.uk
# The support of the Atomic and Molecular Data Unit of the IAEA
# during the development of this library is gratefully acknowledged.
#
# This file is part of PyValem
#
# PyValem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyValem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyValem.  If not, see <http://www.gnu.org/licenses/>

import sys
import re
import pyparsing as pp
from atom_data import element_symbols, atom_data

element = pp.oneOf(element_symbols)
# TODO don't allow leading 0
integer = pp.Word(pp.nums)
plusminus = pp.Literal('+') | pp.Literal('-')

# An isotope looks like '(1H)', '(13C)', etc.; strip the parentheses
isotope = pp.Group(pp.Suppress(pp.Literal('(')) + integer + element
                + pp.Suppress(pp.Literal(')')))

# some named components of a formula
# stoich comes before or after a "bare" element symbol, e.g. 3Br2
stoich = pp.Optional(integer, default='1').setResultsName('stoich')
# prestoich comes before a bracketed element group, e.g. 2(NH3)
prestoich = pp.Optional(integer, default='1').setResultsName('prestoich')
# poststoich comes after a bracketed element group, e.g. (H2O)3
poststoich = pp.Optional(integer, default='1').setResultsName('poststoich')
# the charge is always defined and defaults to '0'
charge = pp.Optional(pp.Combine(pp.Group(plusminus + pp.Optional(integer,
                        default='1'))), default='0').setResultsName('charge')
# An elementRef is either an element symbol or an isotope symbol plus a
# stoichiometry which is 1 if not given
elementRef = pp.Group((isotope | element).setResultsName('atom_symbol')+stoich)
# A chemicalFormula is a series of elementRefs
chemicalFormula = pp.Group(pp.OneOrMore(elementRef)).setResultsName('atoms')
# Radicals must be specified with the unicode character '·' (U+00B7)
radicalDot = pp.Optional(u'·').setResultsName('radical')

# A chargedChemicalFormula is a chemicalFormula with an optional pre-
# stoichiometry, radical dot and charge
chargedChemicalFormula= pp.Group(stoich + chemicalFormula + radicalDot + charge)

# A bracketedChemicalFormula is essentially a chargedChemicalFormula inside
# parentheses with optional pre- and post-stoichiometries
bracketedChemicalFormula = pp.Group((prestoich + pp.Suppress(pp.Literal('('))
                            + chemicalFormula + radicalDot + charge
                            + pp.Suppress(pp.Literal(')')) + poststoich))

# A chemical_formula_fragment is either one of the above ChemicalFormula
# types, optionally prefixed with a period ('.')
chemical_formula_fragment = pp.Optional(pp.Suppress('.'))\
            + (chargedChemicalFormula | bracketedChemicalFormula)
chemical_formula_fragments = pp.OneOrMore(chemical_formula_fragment)\
                            .setResultsName('formula')

# These are the formula prefix tokens we recognise and their slugs
# NB be careful to ensure that the slugs remain case-insensitive!
# For example, '(S)-' -> 'S-' but 's-' -> 'syn-'
prefix_tokens = {'(+)': 'p', '(-)': 'm', u'(±)': 'pm', 'D': 'D', 'L': 'L',
                 '(R)': 'R', '(S)': 'S', '(E)': 'E', '(Z)': 'Z',
                 'cis': 'cis', 'trans': 'trans', 's': 'syn', 'a': 'anti',
                 u'Δ': 'Delta', u'Λ': 'Lambda',
                 u'α': 'alpha', u'β': 'beta', u'γ': 'gamma',
                 'n': 'n', 'i': 'i', 't': 't', 'neo': 'neo', 'sec': 'sec',
                 'o': 'o', 'm': 'm', 'p': 'p',
                 'ortho': 'ortho', 'meta': 'meta', 'para': 'meta',}
# also allow a comma-separated list of integers, e.g. 1,1,2-
prefix_parser = pp.delimitedList(pp.OneOrMore(integer), combine=True)
for pt in prefix_tokens.keys():
    prefix_parser |= pp.Literal(pt)
# Any number of prefix tokens may appear, separated by a hyphen
prefix_list_parser = (pp.delimitedList(prefix_parser, delim='-')#, combine=True)
                        + pp.Suppress(pp.Literal('-'))).setResultsName('prefix')

# TODO (2R,3R)- (2R, 3S)-, etc...

# Finally, a complexChemicalFormula is a prefix, followed by one or more
# chemical_formula_fragments
complexChemicalFormula = pp.Optional(prefix_list_parser)\
                         + chemical_formula_fragments + pp.StringEnd()

slug_charge_sign = {'+': 'p', '-': 'm'}

# Some Exceptions
class ChemFormulaError(Exception):
    def __init__(self, error_str):
        self.error_str = error_str
    def __str__(self):
        return self.error_str

class ChemFormulaParseError(Exception):
    def __init__(self, error_str):
        self.error_str = error_str
    def __str__(self):
        return self.error_str

class ChemFormula(object):
    """
    A class representing a chemical formula, with methods for parsing and
    transforming its appearance as text or HTML.

    """

    def __init__(self, formula):
        """
        Initialize the ChemFormula object by parsing the string argument
        formula.

        """

        self.formula = formula
        self.parse_formula(formula)

    def make_prefix_html(self, prefix_list):
        """
        Make the prefix HTML:
            D- and L- prefixes get written in small caps
        """
        prefix = '-'.join(prefix_list)
        prefix = prefix.replace('D', '<span style="font-size: 80%;">D</span>')
        prefix = prefix.replace('L', '<span style="font-size: 80%;">L</span>')
        return '%s-' % prefix

    def make_prefix_slug(self, prefix_list):
        """
        Make the prefix slug: commas are replaced by underscores and non-ASCII
        characters swapped out according to the entries in the prefix_tokens
        dictionary. For example,
            1,1,3- -> 1_1_3-
            (±)- -> pm-
            (α)- -> alpha-
        """
        slug_prefix_tokens = []
        for prefix_token in prefix_list:
            # TODO don't allow matches including numbers with leading zeros
            if re.match('^\d+(,\d+)*$', prefix_token):
                # this prefix token is a comma-separated list of numbers
                slug_prefix_token = prefix_token.replace(',', '_')
            else:
                # select the slug version of this prefix from prefix_tokens
                try:
                    slug_prefix_token = prefix_tokens[prefix_token]
                except KeyError:
                    raise ChemFormulaParseError('Unrecognised formula prefix'
                                ' token: %s' % prefix_token)
            slug_prefix_tokens.append(slug_prefix_token)
        slug_prefix = '-'.join(slug_prefix_tokens)
        return '%s__' % slug_prefix

    def parse_formula(self, formula):
        try:
            moieties = complexChemicalFormula.parseString(formula)
        except pp.ParseException:
            raise ChemFormulaParseError('Invalid formula syntax: %s' % formula)

        self.atom_stoich = {}
        self.charge = 0
        html_chunks = []
        slug_chunks = []
        # calculate relative molecular mass as the sum of the atomic weights
        self.rmm = 0.

        # make the prefix html and slug
        try:
            html_chunks.append(self.make_prefix_html(moieties['prefix']))
            slug_chunks.append(self.make_prefix_slug(moieties['prefix']))
        except KeyError:
            # no prefix
            pass

        moieties = moieties['formula']
        for moiety in moieties:
            if 'prestoich' in moiety.keys():
                # bracketed fragment, e.g. (OH)2, 3(HO2+), ...
                prestoich = int(moiety['prestoich'])
                if prestoich > 1:
                    slug_chunks.append(moiety['prestoich'])
                    html_chunks.append(moiety['prestoich'])
                html_chunks.append('(')
                slug_chunks.append('_')
                poststoich = int(moiety['poststoich'])
                stoich = prestoich * poststoich
            else:
                # unbracketed fragment, e.g. H2O, 2NH3, ...
                stoich = int(moiety['stoich'])
                if stoich > 1:
                    slug_chunks.append(moiety['stoich'])
                    html_chunks.append(moiety['stoich'])
            charge = int(moiety['charge'])
            self.charge += charge * stoich
            for atom in moiety['atoms']:
                atom_symbol, atom_stoich = atom

                if isinstance(atom_symbol, pp.ParseResults):
                    # we got an isotope in the form '(zSy)' with z the mass
                    # number so symbol is the ParseResults ['z', 'Sy']:
                    mass_number,atom_symbol = int(atom_symbol[0]),atom_symbol[1]
                    symbol_html = '<sup>%d</sup>%s' % (mass_number, atom_symbol)
                    atom_symbol = '%d%s' % (mass_number, atom_symbol)
                    slug_chunks.append('-%s' % atom_symbol)
                else:
                    mass_number = 0
                    symbol_html = atom_symbol
                    slug_chunks.append(atom_symbol)
                try:
                    Z, atomic_weight = atom_data[atom_symbol][:2]
                except KeyError:
                    raise ChemFormulaParseError('Unknown element symbol'
                               ' %s in formula %s' % (atom_symbol, formula))

                atom_stoich = int(atom_stoich)
                total_atom_stoich = atom_stoich * stoich
                self.rmm += atomic_weight * total_atom_stoich
                try:
                    self.atom_stoich[(Z, mass_number)] += total_atom_stoich
                except KeyError:
                    self.atom_stoich[(Z, mass_number)] = total_atom_stoich

                html_chunks.append(symbol_html)
                if atom_stoich > 1:
                    html_chunks.append('<sub>%d</sub>' % atom_stoich)
                    slug_chunks.append(str(atom_stoich))

            moiety_charge_html, moiety_charge_slug=self._get_charge_reps(charge)
            html_chunks.append(moiety_charge_html)
            slug_chunks.append(moiety_charge_slug)

            if 'poststoich' in moiety.keys():
                html_chunks.append(')')
                slug_chunks.append('_')
                if poststoich > 1:
                    html_chunks.append('<sub>%d</sub>' % poststoich)
                    slug_chunks.append('%d' % poststoich)

            if 'radical' in moiety.keys():
                html_chunks.append('&#183;')
                slug_chunks.append('_dot')

        self.html = ''.join(html_chunks)
        # strip the leading '-' if the formula began with an isotope
        self.slug = ''.join(slug_chunks).lstrip('-')

    def _get_charge_reps(self, charge):
        if charge:
            s_charge = ''
            if abs(charge) > 1:
                s_charge = str(abs(charge))
            s_charge_sign = '+'
            if charge < 0:
                s_charge_sign = '-'
            moiety_charge_html = '<sup>%s%s</sup>' % (s_charge,s_charge_sign)
            moiety_charge_slug = '_%s%s' % (slug_charge_sign[s_charge_sign],
                                            s_charge)
            return moiety_charge_html, moiety_charge_slug
        return '', ''
                
    def parse_formula_old(self, formula):
        """
        Parse the string formula into a dictionary of element symbols and
        an (integer) charge value.

        """

        self.atom_stoich = {}
        try:
            chargedformulaData = chargedChemicalFormula.parseString(formula)
        except ParseException:
            raise ChemFormulaParseError('Invalid formula syntax: %s' % formula)
        formulaData = chargedformulaData[0]
        
        # parse the charge part of the formula, if present:
        try:
            self.charge_sign, charge_value = chargedformulaData[1]
            self.charge = int('%s%s' % (self.charge_sign, charge_value))
        except IndexError:
            self.charge = 0

        html_chunks = []
        slug_chunks = []
        # calculate the relative molecular mass as the sum of the
        # atomic weights
        self.rmm = 0.
        for symbol, stoich in formulaData:
            istoich = int(stoich)
            if isinstance(symbol, ParseResults):
                # we got an isotope in the form '(zSy)' with z the mass number
                # so symbol is the ParseResults ['z', 'Sy']:
                mass_number, symbol = int(symbol[0]), symbol[1]
                symbol_html = '<sup>%d</sup>%s' % (mass_number, symbol)
                symbol = '%d%s' % (mass_number, symbol)
                slug_chunks.append('-%s' % symbol)
            else:
                # a regular element symbol (no mass number needed)
                mass_number = 0
                symbol_html = symbol
                slug_chunks.append(symbol)

            # get the atomic number and weight for this isotope or element
            try:
                atomic_number, atomic_weight = atom_data[symbol][:2]
            except KeyError:
                raise ChemFormulaParseError('Unknown element symbol %s in'
                              ' formula %s' % (symbol, formula))
            try:
                self.atom_stoich[(atomic_number, mass_number)] += istoich
            except KeyError:
                self.atom_stoich[(atomic_number, mass_number)] = istoich

            self.rmm += atomic_weight * istoich

            html_chunks.append(symbol_html)
            if istoich > 1:
                html_chunks.append('<sub>%d</sub>' % istoich)
                slug_chunks.append(str(istoich))

        if self.charge:
            s_charge = ''
            if abs(self.charge) > 1:
                s_charge = str(abs(self.charge))
            html_chunks.append('<sup>%s%s</sup>' % (s_charge,
                                                    self.charge_sign))
            slug_chunks.append('_%s%s' % (slug_charge_sign[self.charge_sign],
                                          s_charge))
        self.html = ''.join(html_chunks)
        # strip the leading '-' if the formula began with an isotope
        self.slug = ''.join(slug_chunks).lstrip('-')

    def __str__(self):
        return self.formula

    def _stoichiometric_formula_atomic_number(self, atom_stoich_keys):
        atom_strs = []
        for atomic_number, mass_number in sorted(atom_stoich_keys):
            symbol = atom_data[(atomic_number, mass_number)][3]
            if mass_number:
                symbol = '(%s)' % symbol
            atom_strs.append(self._get_symbol_stoich(symbol,
                            self.atom_stoich[(atomic_number,mass_number)]))
        return atom_strs

    def _stoichiometric_formula_alphabetical(self, atom_stoich_keys):
        atom_strs = self._stoichiometric_formula_atomic_number(atom_stoich_keys)
        atom_strs.sort()
        return atom_strs

    def stoichiometric_formula(self, fmt='atomic number'):
        """
        Return a string representation of the stoichiometric formula
        in one of the formats specified by the fmt argument:
        "atomic number": order atoms by increasing atomic number
        "alphabetical" : order atoms in alphabetical order of atomic symbol
        "hill": the Hill system for organic molecules - first C, then H,
                then the remaining atoms in alphabetical order.

        """

        fmt = fmt.lower()
        if fmt not in ('atomic number', 'hill', 'alphabetical'):
            raise ChemFormulaError('Unsupported format for stoichiometric'
                    ' formula output: %s' % fmt)

        if fmt == 'atomic number':
            atom_strs = self._stoichiometric_formula_atomic_number(
                                                    self.atom_stoich.keys())
        elif fmt == 'alphabetical':
            atom_strs = self._stoichiometric_formula_alphabetical(
                                                    self.atom_stoich.keys())
        elif fmt == 'hill':
            # Hill system: if the formula contains C, then C comes first,
            # followed by H (if present), and then the other elements' symbols
            # in alphabetical order
            atom_strs = []
            carbon_keys = self._get_atom_stoich_keys_from_atomic_number(6)
            if carbon_keys:
                for carbon_key in carbon_keys:
                    symbol = atom_data[carbon_key][3]
                    if carbon_key[1]:   # isotope of C
                        symbol = '(%s)' % symbol
                    atom_strs.append(self._get_symbol_stoich(symbol,
                                self.atom_stoich[carbon_key]))
                hydrogen_keys = self._get_atom_stoich_keys_from_atomic_number(1)
                for hydrogen_key in hydrogen_keys:
                    symbol = atom_data[hydrogen_key][3]
                    if hydrogen_key[1]: # isotope of H
                        symbol = '(%s)' % symbol
                    atom_strs.append(self._get_symbol_stoich(symbol,
                                self.atom_stoich[hydrogen_key]))
            # get a list of the atom_stoich_keys omitting C and H
            atom_stoich_keys = []
            for atom_stoich_key in self.atom_stoich.keys():
                if atom_stoich_key[0] not in (1,6):
                    atom_stoich_keys.append(atom_stoich_key)
            # the remaining element symbols appear in alphabetical order
            atom_strs.extend(self._stoichiometric_formula_alphabetical(
                                                    atom_stoich_keys))

        # finally, add on the charge string, e.g. '', '-', '+2', ...
        atom_strs.append(self._get_charge_string())
        return ''.join(atom_strs)

    def _get_atom_stoich_keys_from_atomic_number(self, atomic_number):
        """
        Return a list of atom_stoich_keys corresponding to elements
        with a  given atomic_number.

        """

        atom_stoich_keys = []
        for atom_stoich_key in self.atom_stoich.keys():
            if atom_stoich_key[0] == atomic_number:
                atom_stoich_keys.append(atom_stoich_key)
        return atom_stoich_keys

    def _get_symbol_stoich(self, symbol, stoich):
        """
        Return Xn for element symbol X and stoichiometry n, unless n is 1,
        in which case, just return X.

        """
        if stoich > 1:
            return '%s%d' % (symbol, stoich)
        return symbol

    def _get_charge_string(self):
        """
        Return the string representation of the charge: '+', '-', '+2', '-3',
        etc.

        """

        if not self.charge:
            return ''
        if self.charge > 0:
            if self.charge  > 1:
                return '+%d' % self.charge
            return '+'
        if self.charge == -1:
            return '-'
        return str(self.charge)
