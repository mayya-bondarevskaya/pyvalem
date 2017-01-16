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
        x1 = GenericExcitedState('**')
        x2 = GenericExcitedState('***')
        
        x3 = GenericExcitedState('3*')
        self.assertEqual(x3.int_n,3)
        
        x4 = GenericExcitedState('15*')
        self.assertEqual(x4.int_n,15)
        
        self.assertRaises(StateParseError, GenericExcitedState, 'a')
        self.assertRaises(StateParseError, GenericExcitedState, '*3')
        self.assertRaises(StateParseError, GenericExcitedState, '3 *')
        self.assertRaises(StateParseError, GenericExcitedState, '3**')
        self.assertRaises(StateParseError, GenericExcitedState, '3**?')
        self.assertRaises(StateParseError, GenericExcitedState, '*4**')


if __name__ == '__main__':
    unittest.main()

