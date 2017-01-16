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
    'Σ-', 'Σ-u', 'Σ-g',
    'SIGMA-', 'SIGMA-u', 'SIGMA-g',
    'Σ+', 'Σ+u', 'Σ+g', 
    'SIGMA+', 'SIGMA+u', 'SIGMA+g',
    'Π', 'Πu', 'Πg', 
    'PI', 'PIu', 'PIg',
    'Δ','Δu','Δg',
    'DELTA', 'DELTAu', 'DELTAg',
    'Φ', 'Φg', 'Φu',
    'PHI', 'PHIg', 'PHIu',
    'A', "A'", 'A"', 'A1', "A'1", 'A"1', 'A2', "A'2", 'A"2', 'A3',
    'Ag', "A'g", 'A"g', 'A1g', 'A2g', 'A3g',
    'Au', "A'u", 'A"u', 'A1u', 'A2u', 'A3u',
    'B', "B'", 'B"', 'B1', 'B2', 'B3',
    'Bg', "B'g", 'B"g', 'B1g', 'B2g', 'B3g',
    'Bu', "B'u", 'B"u', 'B1u', 'B2u', 'B3u',
    'E', "E'", 'E"', 'E1', "E'1", 'E"1', 'E2', "E'2", 'E"2',
    'E3', "E'3", 'E"3', 'E4', 'E5', 'E6', 'E7',
    'Eg', "E'g", 'E"g', 'E1g', 'E2g', 'E3g',
    'Eu', "E'u", 'E"u', 'E1u', 'E2u', 'E3u',
    'T', 'T1', 'T2',
    'Tg', 'T1g', 'T2g',
    'Tu', 'T1u', 'T2u',
    'G', 'Gg', 'Gu',
    'H', 'Hg', 'Hu'
)

greek_letters = {'SIGMA-': 'Σ-',
                 'SIGMA-u': 'Σ-u',
                 'SIGMA-g': 'Σ-g',
                 'SIGMA+': 'Σ+',
                 'SIGMA+u': 'Σ+u',
                 'SIGMA+g': 'Σ+g',
                 'PI': 'Π',
                 'PIu': 'Πu',
                 'PIg': 'Πg',
                 'DELTA': 'Δ',
                 'DELTAu': 'Δu',
                 'DELTAg': 'Δg',
                 'PHI': 'Φ',
                 'PHIg': 'Φg',
                 'PHIu': 'Φu'}

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
        pp.Suppress(pp.Optional('(')) + molecule_term +
        pp.Suppress(pp.Optional(')'))
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
        irrep = components.irrep
        if (irrep in greek_letters.keys()):
            irrep = greek_letters[irrep]
            
        self.irrep = irrep
        self.term_label = components.term_label or None
        self.J = parse_fraction(components.Jstr)

    def irrep_html(self, irrep):
        irrep_chunks = []
        if '+' in irrep or '-' in irrep:
            irrep_chunks.append('{0:s}<sup>{1:s}</sup>'
                                    .format(irrep[0],irrep[1]))
            next_idx = 2
        elif '"' in irrep or "'" in irrep:
            irrep_chunks.append(irrep[0:2])
            next_idx = 2
        else:
            irrep_chunks.append(irrep[0])
            next_idx = 1
        if irrep[next_idx:] is not '':
            irrep_chunks.append('<sub>{:s}</sub>'.format(irrep[next_idx:]))
        return ''.join(irrep_chunks)
        
    @property
    def html(self):
        """Return an HTML representation of the MolecularTermSymbol."""

        # TODO Handle terms with superscripts and subscripts more gracefully.

        html_chunks = []
        if self.term_label is not None:
            html_chunks.append('{:s}('.format(self.term_label))
        html_chunks.append('<sup>{0:d}</sup>{1:s}'
                              .format(self.Smult, self.irrep_html(self.irrep)))
        if self.J is not None:
            if self.J.is_integer():
                Jstr = str(int(self.J))
            else:
                Jstr = '{0:d}/2'.format(int(2*self.J))
            html_chunks.append('<sub>{0:s}</sub>'.format(Jstr))
        if self.term_label is not None:
            html_chunks.append(')')
        return ''.join(html_chunks)
