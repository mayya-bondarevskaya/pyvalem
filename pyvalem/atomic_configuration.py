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
noble_gases = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
noble_gas_configs = {'He': '1s2',
                     'Ne': '[He].2s2.2p6',
                     'Ar': '[Ne].3s2.3p6',
                     'Kr': '[Ar].3d10.4s2.4p6',
                     'Xe': '[Kr].4d10.5s2.5p6',
                     'Rn': '[Xe].4f14.5d10.6s2.6p6'
                    }

noble_gas = pp.oneOf(['[{}]'.format(symbol) for symbol in noble_gases])

atom_orbital = pp.Group(integer.setResultsName('n') +
                pp.oneOf(atomic_orbital_symbols).setResultsName('lletter') + 
                integer.setResultsName('nocc')
               )

atom_config = ((atom_orbital | noble_gas) +
            pp.ZeroOrMore(pp.Suppress('.') + atom_orbital).leaveWhitespace() +
            pp.StringEnd() ).leaveWhitespace()

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

        # Expand out noble gas notation, if used, and check that the
        # subshells 1s, 2s, 2p, ... are unique.
        subshells = self.expand_noble_gas_config(self.state_str)
        subshells = [subshell[:2] for subshell in subshells.split('.')]

        self.orbitals = []
        for i, parsed_orbital in enumerate(parse_results):
            if not i and type(parsed_orbital) == str:
                # Noble-gas notation for first atomic orbital
                continue
            # Create a validated AtomicOrbital object for this orbital.
            orbital = AtomicOrbital(n=parsed_orbital['n'],
                                    lletter=parsed_orbital['lletter'],
                                    nocc=parsed_orbital['nocc'])
            self.orbitals.append(orbital)

        # Check that the subshells specified are unique
        if len(subshells) != len(set(subshells)):
            raise AtomicConfigurationError('Repeated subshell in {0}'
                                                    .format(state_str))

    def expand_noble_gas_config(self, config):
        """Recursively expand out the noble gas notation to orbitals.

        For example, '[He].2s1' -> '1s2.2s2',
        '[Xe].4f7' -> '1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6.4d10.5s2.5p6.4f7'

        """

        if config[0] != '[':
            return config
        return (self.expand_noble_gas_config(noble_gas_configs[config[1:3]]) +
                config[4:])
