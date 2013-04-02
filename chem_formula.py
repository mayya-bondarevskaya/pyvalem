# -*- coding: utf-8 -*-
# chem_formula.py

# Christian Hill, 2/4/13
# Department of Physics and Astronomy, University College London
# christian.hill@ucl.ac.uk

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
            charge_sign, charge_value = chargedformulaData[1]
            self.charge = int('%s%s' % (charge_sign, charge_value))
        except IndexError:
            self.charge = 0

        # calculate the relative molecular mass as the sum of the
        # atomic weights
        self.rmm = 0.
        for symbol, stoich in formulaData:
            istoich = int(stoich)
            try:
                atomic_number, atomic_weight = atom_data[symbol][:2]
            except KeyError:
                raise ChemFormulaParseError('Unknown element symbol %s in'                              ' formula %s' % (symbol, formula))
            self.rmm += atomic_weight * istoich
            try:
                self.atom_stoich[atomic_number] += istoich
            except KeyError:
                self.atom_stoich[atomic_number] = istoich

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
            for atomic_number in sorted(self.atom_stoich.keys()):
                atom_strs.append(self._get_symbol_stoich(
                                        atom_data[atomic_number][2],
                                        self.atom_stoich[atomic_number]))
            if fmt == 'alphabetical':
                atom_strs.sort()
        elif fmt == 'hill':
            # Hill system: if the formula contains C, then C comes first,
            # followed by H (if present), and then the other elements' symbols
            # in alphabetical order
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
