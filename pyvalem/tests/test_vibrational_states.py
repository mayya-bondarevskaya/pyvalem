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
        v0 = VibrationalState('0')
        self.assertEqual(v0.html, 'v=0')
        self.assertEqual(str(v0), 'v=0')
        
        v1 = VibrationalState('v=5')
        self.assertEqual(v1.html, 'v=5')
        self.assertEqual(str(v1), 'v=5')
        
        v2 = VibrationalState('3v2+v3')
        self.assertEqual(str(v2), '3ν2+ν3')
        self.assertEqual(v2.html, '3ν<sub>2</sub> + ν<sub>3</sub>')
        
        v3 = VibrationalState('ν1+ν2')
        self.assertEqual(str(v3), 'ν1+ν2')
        self.assertEqual(v3.html, 'ν<sub>1</sub> + ν<sub>2</sub>')
        
        v4 = VibrationalState('2v1 + 3v4')
        self.assertEqual(str(v4), '2ν1+3ν4')
        self.assertEqual(v4.html, '2ν<sub>1</sub> + 3ν<sub>4</sub>')

        v5 = VibrationalState('3v2')
        self.assertTrue(v5.polyatomic)
        self.assertEqual(str(v5), '3ν2')
        self.assertEqual(v5.html, '3ν<sub>2</sub>')

        self.assertRaises(StateParseError, VibrationalState, 'abc')
        self.assertRaises(StateParseError, VibrationalState, 'v+v2')
        self.assertRaises(StateParseError, VibrationalState, '1v1+')

    def test_generic_excited_vibrational_state(self):
        v1 = VibrationalState('v=*')
        self.assertIsNone(v1.polyatomic)
        self.assertEqual(str(v1), 'v=*')
        self.assertEqual(v1.html, 'v=*')

        v2 = VibrationalState('**')
        self.assertEqual(str(v2), 'v=**')
        self.assertEqual(v2.html, 'v=**')

        self.assertRaises(StateParseError, VibrationalState, 'v=****')
       

if __name__ == '__main__':
    unittest.main()
