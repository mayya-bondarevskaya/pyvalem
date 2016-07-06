# state.py
# Version 1.1
# A class representing an atomic or molecular state, parsing various State
# objects into existence from text strings.
#
# Copyright (C) 2012-2016 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
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
import pyparsing as pp

atom_L_symbols = ('S', 'P', 'D', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O',
                  'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
atom_orbital_symbols = tuple(s.lower() for s in atom_L_symbols)

integer = pp.Word(pp.nums)

atom_Smult = integer.setResultsName('Smult')
atom_Lletter = pp.oneOf(atom_L_symbols).setResultsName('Lletter')
atom_Jstr = (integer + pp.Optional(pp.Suppress('/')+'2')).setResultsName('Jstr')
atom_parity = pp.Literal('o').setResultsName('parity')
atom_term = (atom_Smult + atom_Lletter + pp.Optional(atom_parity) +
             pp.Optional(pp.Suppress('_') + atom_Jstr))

class State(object):
    def __init__(self, state_str):
        self.state_str = state_str
        self.parse_state(state_str)

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
        self.J = None
        if len(components.Jstr) == 2:
            num, det = components.Jstr
            self.J = float(num) / int(det)
        else:
            if components.Jstr:
                self.J = float(components.Jstr[0])
        if self.J is not None:
            self.validate_J()
                
    def validate_J(self):
        if not abs(self.L - self.S) <= self.J <= self.L + self.S:
            raise StateParseError('Invalid atomic term symbol: {0:s}'
                ' |L-S| <= J <= L+S must be satisfied.'.format(self.state_str))

    @property
    def html(self):
        html_chunks = ['<sup>{0:d}</sup>{1:s}'.format(self.Smult, self.Lletter)]
        if self.parity:
            html_chunks.append('<sup>o</sup')
        if self.J is not None:
            if self.J.is_integer():
                Jstr = str(int(self.J))
            else:
                Jstr = '{0:d}/2'.format(int(2*self.J))
            html_chunks.append('<sub>{0:s}</sub>'.format(Jstr))
        return ''.join(html_chunks)
