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
from .utils import parse_fraction

orbital_irrep_labels = (
    'Σ-', 'Σ+', 'Π', 'Δ',
    'Σ-u', 'Σ+u', 'Πu', 'Δu',
    'Σ-g', 'Σ+g', 'Πg', 'Δg',
    'A', "A'", 'A"', 'A1', 'A2', 'A3',
    'Ag', "A'g", 'A"g', 'A1g', 'A2g', 'A3g',
    'Au', "A'u", 'A"u', 'A1u', 'A2u', 'A3u',
    'B', "B'", 'B"', 'B1', 'B2', 'B3',
    'Bg', "B'g", 'B"g', 'B1g', 'B2g', 'B3g',
    'Bu', "B'u", 'B"u', 'B1u', 'B2u', 'B3u',
    'E', "E'", 'E"', 'E1', 'E2',
    'Eg', "E'g", 'E"g', 'E1g', 'E2g',
    'Eu', "E'u", 'E"u', 'E1u', 'E2u',
    'T1', 'T2',
    'Tg', 'Tu',
    'T1g', 'T1u', 'T2g', 'T1u',
)

integer = pp.Word(pp.nums)
molecule_Smult = integer.setResultsName('Smult')
molecule_irrep = pp.oneOf(orbital_irrep_labels).setResultsName('irrep')
molecule_Jstr = (pp.Combine(pp.Optional(pp.oneOf(('+','-'))) +
                 integer) +
                 pp.Optional(pp.Suppress('/')+'2')).setResultsName('Jstr')
molecule_term = (molecule_Smult + molecule_irrep +
                 pp.Optional(pp.Suppress('_') + molecule_Jstr))
term_label = pp.Combine(pp.Word(pp.srange('[A-Za-z]')) +
                        pp.Optional(pp.oneOf(("'", '"')))
                       ).setResultsName('term_label')
molecule_term_with_label = (
        pp.Optional(term_label) +
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
        self.Smult = int(components.Smult)
        self.irrep = components.irrep
        self.term_label = components.term_label or None
        self.J = parse_fraction(components.Jstr)

    @property
    def html(self):
        # Mayya TODO

        return ''.join(html_chunks)
