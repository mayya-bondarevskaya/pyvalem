# test_state.py
# Unit tests for the state module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..molecular_term_symbol import MolecularTermSymbol
from ..generic_excited_state import GenericExcitedState

class GenericExcitedStateTest(unittest.TestCase):
    def test_generic_excited_term_symbol(self):
        x0 = GenericExcitedState('*')
        self.assertEqual(x0.html, '<sup>*<\sup>')
        x1 = GenericExcitedState('**')
        self.assertEqual(x1.html, '<sup>**<\sup>')
        x2 = GenericExcitedState('***')
        self.assertEqual(x2.html, '<sup>***<\sup>')
        
        x3 = GenericExcitedState('3*')
        self.assertEqual(x3.int_n,3)
        self.assertEqual(x3.html, '3<sup>*<\sup>')
        
        x4 = GenericExcitedState('15*')
        self.assertEqual(x4.int_n,15)
        self.assertEqual(x4.html, '15<sup>*<\sup>')
        
        self.assertRaises(StateParseError, GenericExcitedState, 'a')
        self.assertRaises(StateParseError, GenericExcitedState, '*3')
        self.assertRaises(StateParseError, GenericExcitedState, '3 *')
        self.assertRaises(StateParseError, GenericExcitedState, '3**')
        self.assertRaises(StateParseError, GenericExcitedState, '3**?')
        self.assertRaises(StateParseError, GenericExcitedState, '*4**')


if __name__ == '__main__':
    unittest.main()

