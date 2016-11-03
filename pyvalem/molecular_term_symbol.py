# The MolecularTermSymbol class, representing a molecular term symbol, with
# methods for parsing a string into quantum numbers and labels, creating
# an HTML representation of the term symbol, etc.
#
# Copyright (C) 2012-2016 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
#
# This file is part of PyValem

import pyparsing as pp
from .state import State, StateParseError

orbital_irrep_labels = (
    'Σ-', 'Σ-u', 'Σ-g',
    'Σ+', 'Σ+u', 'Σ+g', 
    'Π', 'Πu', 'Πg', 
    'Δ','Δu','Δg',
    'Φ', 'Φg', 'Φu',
    'A', "A'", 'A"', 'A1', "A'1", 'A"1', 'A2', "A'2", 'A"2', 'A3',
    'Ag', "A'g", 'A"g', 'A1g', 'A2g', 'A3g',
    'Au', "A'u", 'A"u', 'A1u', 'A2u', 'A3u',
    'B', "B'", 'B"', 'B1', 'B2', 'B3',
    'Bg', "B'g", 'B"g', 'B1g', 'B2g', 'B3g',
    'Bu', "B'u", 'B"u', 'B1u', 'B2u', 'B3u',
    'E', "E'", 'E"', 'E1', "E'1", 'E"1', 'E2', "E'2", 'E"2', 'E3', "E'3", 'E"3', 'E4', 'E5', 'E6', 'E7',
    'Eg', "E'g", 'E"g', 'E1g', 'E2g', 'E3g',
    'Eu', "E'u", 'E"u', 'E1u', 'E2u', 'E3u',
    'T', 'T1', 'T2',
    'Tg', 'T1g', 'T2g',
    'Tu', 'T1u', 'T2u',
    'G', 'Gg', 'Gu',
    'H', 'Hg', 'Hu'
)

integer = pp.Word(pp.nums)
molecule_Smult = integer.setResultsName('Smult')
molecule_irrep_label = pp.oneOf(orbital_irrep_labels).setResultsName('irrep')
molecule_Jstr = (pp.Optional(pp.oneOf(('+','-'))) +
                 integer +
                 pp.Optional(pp.Suppress('/')+'2')).setResultsName('Jstr')
molecule_term = (molecule_Smult + molecule_irrep_label +
                 pp.Optional(pp.Suppress('_') + molecule_Jstr))
molecule_term_with_label = (pp.Word(pp.srange('[A-Z]')) +
                            pp.Optional(pp.oneOf(("'", '"'))) +
                            pp.Suppress('(') + molecule_term + pp.Suppress(')')
                           )

class MolecularTermSymbol(State):
    def parse_state(self, state_str):
        self.state_str = state_str

        try:
            components = molecule_term_with_label.parseString(state_str)
        except pp.ParseException:
            raise StateParseError('Invalid molecular term symbol syntax: {0}'
                                            .format(state_str))
