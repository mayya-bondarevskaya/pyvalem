# The PhaseState class, representing a phase of matter, substance or material.
# It provides methods for parsing a string into a representation of the state
# of the material (e.g. solid, liquid, gas, adsorbed, ...)
#
# Copyright (C) 2012-2017 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
#
# This file is part of PyValem

from .state import State, StateParseError

class PhaseState(State):
    def parse_state(self, state_str):
        self.state_str = state_str

        if state_str[0] != ':':
            raise StateParseError("A PhaseState must start with ':', but was"
                    ' passed {}'.format(state_str))

        if state_str[:2] == ':s':
            self.phase = 's'
        elif state_str[:2] == ':l':
            self.phase = 'l'
        elif state_str[:2] == ':g':
            self.phase = 'g'
        elif state_str[:2] == ':a':
            self.phase = 'a'
        else:
            raise StateParseError('Unrecognised PhaseState specification: {}'
                    '. Must be one of :s, :l, :g, :a'.format(state_str))

        if self.phase == 'a':
            # resolve substrate specification
            pass

    @property
    def html(self):
        return ':({})'.format(self.phase)


