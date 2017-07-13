# test_phase_state.py
# Unit tests for the "phase state" module of PyValem
#
# Copyright (C) 2012-2017 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..phase_state import PhaseState

class PhaseStateTest(unittest.TestCase):

    def test_phase_state(self):
        for s in [':a', ':s', ':l', ':g']:
            p = PhaseState(s)
            self.assertEqual(p.html, ':({})'.format(s[1]))

        self.assertRaises(StateParseError, PhaseState, 's')
        self.assertRaises(StateParseError, PhaseState, ':q')


if __name__ == '__main__':
    unittest.main()

