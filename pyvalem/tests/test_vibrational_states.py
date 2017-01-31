# test_vibrational_states.py
# Unit tests for the vibrational states module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..vibrational_state import VibrationalState

class VibrationalStateTest(unittest.TestCase):
    def test_vibrational_state(self):
        v0 = VibrationalState('1')
        v1 = VibrationalState('5')
        v2 = VibrationalState('3v2+v3')
        v3 = VibrationalState('v1+v2')
        v4 = VibrationalState('2v1 + 3v4')
        
        self.assertRaises(StateParseError, VibrationalState, 'abc')
        self.assertRaises(StateParseError, VibrationalState, 'v+v2')
        self.assertRaises(StateParseError, VibrationalState, '1v1')


if __name__ == '__main__':
    unittest.main()
