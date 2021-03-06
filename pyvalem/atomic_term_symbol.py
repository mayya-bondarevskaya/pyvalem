# The AtomicTermSymbol class, representing an atomic term symbol, with
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

atom_L_symbols = ('S', 'P', 'D', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O',
                  'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

integer = pp.Word(pp.nums)

atom_Smult = integer.setResultsName('Smult')
atom_Lletter = pp.oneOf(atom_L_symbols).setResultsName('Lletter')
atom_Jstr = (integer+pp.Optional(pp.Suppress('/')+'2')+pp.StringEnd()).setResultsName('Jstr')
atom_parity = pp.Literal('o').setResultsName('parity')
atom_term = (atom_Smult + atom_Lletter + pp.Optional(atom_parity) +
             pp.Optional(pp.Suppress('_') + atom_Jstr) + pp.StringEnd())

class AtomicTermSymbol(State):
    def parse_state(self, state_str):
        self.state_str = state_str

        try:
            components = atom_term.parseString(state_str)
        except pp.ParseException:
            raise StateParseError('Invalid atomic term symbol syntax: {0}'
                                            .format(state_str))
        self.Smult = int(components.Smult)
        self.S = (self.Smult - 1) / 2.
        self.Lletter = components.Lletter
        self.L = atom_L_symbols.index(components.Lletter)
        self.parity = components.get('parity')
        self.J = parse_fraction(components.Jstr)
        if self.J is not None:
            self.validate_J()
                
    def validate_J(self):
        if not abs(self.L - self.S) <= self.J <= self.L + self.S:
            raise StateParseError('Invalid atomic term symbol: {0:s}'
                ' |L-S| <= J <= L+S must be satisfied.'.format(self.state_str))

    @property
    def html(self):
        html_chunks = ['<sup>{0:d}</sup>{1:s}'.format(self.Smult,self.Lletter)]
        if self.parity:
            html_chunks.append('<sup>o</sup>')
        if self.J is not None:
            if self.J.is_integer():
                Jstr = str(int(self.J))
            else:
                Jstr = '{0:d}/2'.format(int(2*self.J))
            html_chunks.append('<sub>{0:s}</sub>'.format(Jstr))
        return ''.join(html_chunks)

