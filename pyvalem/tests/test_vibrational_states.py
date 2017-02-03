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
        self.assertEqual(v0.html, '1')
        
        v1 = VibrationalState('5')
        self.assertEqual(v1.html, '5')
        
        v2 = VibrationalState('3v2+v3')
        self.assertEqual(v2.html, '3v<sub>2<\sub> + 1v<sub>3<\sub>')
        
        v3 = VibrationalState('v1+v2')
        self.assertEqual(v3.html, '1v<sub>1<\sub> + 1v<sub>2<\sub>')
        
        v4 = VibrationalState('2v1 + 3v4')
        self.assertEqual(v4.html, '2v<sub>1<\sub> + 3v<sub>4<\sub>')
        
        self.assertRaises(StateParseError, VibrationalState, 'abc')
        self.assertRaises(StateParseError, VibrationalState, 'v+v2')
        self.assertRaises(StateParseError, VibrationalState, '1v1')


if __name__ == '__main__':
    unittest.main()
