# -*- coding: cp1252 -*-
# The AtomicConfiguration class, representing an atomic electronic
#Â configuration with methods for parsing a string into quantum numbers and
# labels, creating an HTML representation of the term symbol, etc.
#
# Copyright (C) 2012-2016 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
#
# This file is part of PyValem

import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
atomic_orbital_symbols = ('s', 'p', 'd', 'f')

atom_orbital = pp.Group(integer.setResultsName('n') +
                pp.oneOf(atomic_orbital_symbols).setResultsName('lletter') + 
                integer.setResultsName('nocc')
               )

atom_config = (atom_orbital
            + pp.ZeroOrMore(pp.Suppress('.') + atom_orbital).leaveWhitespace()
            + pp.StringEnd() ).leaveWhitespace()

class AtomicConfigurationError(StateParseError):
    pass

class AtomicOrbital:

    def __init__(self, n, l=None, nocc=0, lletter=None):
        self.n = n
        if l is None:
            self.lletter = lletter
            self.l = atomic_orbital_symbols.index(lletter)
        else:
            self.l = l
            self.lletter = atomic_orbital_symbols[l]
        self.nocc = nocc
        self.validate_atomic_orbital()


    def __str__(self):
        return '{}{}{}'.format(self.n, self.lletter, self.nocc)


    def validate_atomic_orbital(self):
        if self.l > self.n - 1:
            raise AtomicConfigurationError('l >= n in atomic orbital {}'
                                                .format(self))
        if self.nocc > 2 * (2*self.l+1):
            raise AtomicConfigurationError('too many electrons in atomic'
                                           ' orbital {}' .format(self))

class AtomicConfiguration(State):

    def parse_state(self, state_str):
        self.state_str = state_str

        try:
            parse_results = atom_config.parseString(state_str)
        except pp.ParseException:
            raise StateParseError('Invalid atomic electronic configuration'
                                  ' syntax: {0}'.format(state_str))

        subshells = [(orbital['n'], orbital['lletter'], orbital['nocc'])
                            for orbital in parse_results]
        if len(subshells) != len(set(subshells)):
            raise AtomicConfigurationError('Repeated subshell in {0}'
                                                    .format(state_str))
        self.orbitals = []
        for parsed_orbital in parse_results:
            orbital = AtomicOrbital(n=parsed_orbital['n'],
                                    lletter=parsed_orbital['lletter'],
                                    nocc=parsed_orbital['nocc'])
