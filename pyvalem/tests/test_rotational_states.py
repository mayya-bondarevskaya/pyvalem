# test_rotational_states.py
# Unit tests for the rotational states module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..rotational_state import RotationalState

class RotationalTermSymbolTest(unittest.TestCase):
    def test_rotational_term_symbol(self):
        rot_state = RotationalState('1/2')
        self.assertEqual(rot_state.J, 0.5)

        rot_state = RotationalState('0')
        self.assertEqual(rot_state.J, 0)
        
        rot_state = RotationalState('2')
        self.assertEqual(rot_state.J, 2)
        
        self.assertRaises(StateParseError, RotationalState, '-2')
        
        self.assertRaises(StateParseError, RotationalState, '1/5')
        self.assertRaises(StateParseError, RotationalState, '1\5')


if __name__ == '__main__':
    unittest.main()
