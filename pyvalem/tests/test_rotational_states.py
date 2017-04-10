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
        self.assertEqual(str(rot_state), 'J=1/2')
        self.assertEqual(rot_state.html, 'J=1/2')

        rot_state = RotationalState('0')
        self.assertEqual(rot_state.J, 0)
        self.assertEqual(str(rot_state), 'J=0')
        self.assertEqual(rot_state.html, 'J=0')
        
        rot_state = RotationalState('2')
        self.assertEqual(rot_state.J, 2)
        
        self.assertRaises(StateParseError, RotationalState, '-2')
        self.assertRaises(StateParseError, RotationalState, 'J=0x')
        
        self.assertRaises(StateParseError, RotationalState, '1/5')
        self.assertRaises(StateParseError, RotationalState, '1/5x')
        self.assertRaises(StateParseError, RotationalState, '1\5')

    def test_generic_excited_rotational_state(self):
        J1 = RotationalState('J=*')
        self.assertEqual(str(J1), 'J=*')
        self.assertEqual(J1.html, 'J=*')

        J2 = RotationalState('**')
        self.assertEqual(str(J2), 'J=**')
        self.assertEqual(J2.html, 'J=**')

        self.assertRaises(StateParseError, RotationalState, 'J=****')
        self.assertRaises(StateParseError, RotationalState, 'J=***z')

if __name__ == '__main__':
    unittest.main()
