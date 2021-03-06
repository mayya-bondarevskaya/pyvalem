# The KeyValuePair class, representing an arbitrary atomic or molecular state,
# with methods for parsing it from a string and outputing its HTML
# representation, etc.
#
# Copyright (C) 2012-2017 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
#
# This file is part of PyValem

from .state import State, StateParseError

class KeyValuePair(State):
    """A class representing an state as an arbitrary key/value pair.

    Any atomic or molecular state that doesn't fit into any of the other
    explicit categories available in PyValem can be represented as a
    key/value pair, parsed in the form 'key=value'.

    """

    def parse_state(self, state_str):
        """Parse state_str into a KeyValuePair object.

        Whitespace is tolerated in the input, i.e both 'key=value' and
        'key = value' are parsed, but no spaces are inserted in the output.

        """

        try:
            key, value = state_str.split('=')
        except ValueError:
            raise StateParseError('Invalid key-value pair: {}.'
                                                .format(state_str))
        self.key = key.strip()
        self.value = value.strip()

        self.state_str = '{}={}'.format(self.key, self.value)
