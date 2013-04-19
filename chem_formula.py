# -*- coding: utf-8 -*-
# chem_formula.py
# A class representing a chemical formula, ChemFormula, and methods for
# parsing ChemFormula objects into existence from text strings.
#
# Copyright (C) 2012 Christian Hill
# Department of Physics and Astronomy, University College London
# christian.hill@ucl.ac.uk
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
from pyparsing import Word, Group, Optional, OneOrMore, ParseException,\
                      Literal, StringEnd, Suppress, ParseResults
from atom_data import atom_data

caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = caps.lower()
digits = '0123456789'
element = Word(caps, lowers)
integer = Word(digits)
isotope = Group(Suppress(Literal('(')) + integer + element
                + Suppress(Literal(')')))
elementRef = Group((isotope | element) + Optional(integer, default='1'))
chemicalFormula = OneOrMore(elementRef)
plusminus = Literal('+') | Literal('-')
charge = Group(plusminus + Optional(integer, default='1'))
chargedChemicalFormula = Group(chemicalFormula) + Optional(charge)\
                            + StringEnd()

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

    def parse_formula(self, formula):
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
            else:
                mass_number = 0
                symbol_html = symbol
            try:
                atomic_number, atomic_weight = atom_data[symbol][:2]
            except KeyError:
                raise ChemFormulaParseError('Unknown element symbol %s in'
                              ' formula %s' % (symbol, formula))
            self.rmm += atomic_weight * istoich
            try:
                self.atom_stoich[(atomic_number, mass_number)] += istoich
            except KeyError:
                self.atom_stoich[(atomic_number, mass_number)] = istoich
            html_chunks.append(symbol_html)
            if istoich > 1:
                html_chunks.append('<sub>%d</sub>' % istoich)
        if self.charge:
            s_charge = ''
            if abs(self.charge) > 1:
                s_charge = str(abs(self.charge))
            html_chunks.append('<sup>%s%s</sup>' % (s_charge,
                                                    self.charge_sign))
        self.html = ''.join(html_chunks)

    def __str__(self):
        return self.formula

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

        if fmt in ('atomic number', 'alphabetical'):
            # Create a list of atom symbols, with their stoichiometries, in
            # order of increasing atomic number
            atom_strs = []
            for atomic_number, mass_number in sorted(self.atom_stoich.keys()):
                symbol = atom_data[(atomic_number, mass_number)][3]
                if mass_number:
                    symbol = '(%s)' % symbol
                atom_strs.append(self._get_symbol_stoich(symbol,
                                self.atom_stoich[(atomic_number,mass_number)]))
            if fmt == 'alphabetical':
                atom_strs.sort()
        elif fmt == 'hill':
            # Hill system: if the formula contains C, then C comes first,
            # followed by H (if present), and then the other elements' symbols
            # in alphabetical order
            # XXX fix this for isotopologues
            return 'NotImplemented'
            if 6 in self.atom_stoich.keys():
                atom_strs = []
                atom_strs.append(self._get_symbol_stoich('C',
                                                         self.atom_stoich[6]))
                offset = 1
                if 1 in self.atom_stoich.keys():
                    offset = 2
                    atom_strs.append(self._get_symbol_stoich('H',
                                                        self.atom_stoich[1]))
                for atomic_number in self.atom_stoich.keys():
                    if atomic_number not in (1,6):
                        atom_strs.append(self._get_symbol_stoich(
                                atom_data[atomic_number][2],
                                self.atom_stoich[atomic_number]))
                atom_strs[offset:].sort()
            else:
                # if the formula does not contain C, all elements (including H)
                # are listed alphabetically
                atom_strs.sort()

        # finally, add on the charge string, e.g. '', '-', '+2', ...
        atom_strs.append(self._get_charge_string())
        return ''.join(atom_strs)

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
