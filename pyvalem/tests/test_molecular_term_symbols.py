#!/usr/bin/python
# -*- coding: utf-8 -*-

# test_molecular_term_symbols.py
# Unit tests for the molecular term symbol module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..molecular_term_symbol import MolecularTermSymbol

class MolecularTermSymbolTest(unittest.TestCase):

    def test_molecular_term_symbol(self):
        c0 = MolecularTermSymbol('X(3Π)')
        self.assertEqual(c0.Smult, 3)
        self.assertEqual(c0.irrep, 'Π')
        self.assertEqual(c0.term_label, 'X')
        #self.assertEqual(c0.html, 'X(<sup>3</sup>Π)')

        c1 = MolecularTermSymbol('(2A")')
        self.assertEqual(c1.irrep, 'A"')
        self.assertIsNone(c1.term_label)
        self.assertEqual(c1.html,'<sup>2</sup>A"')

        self.assertRaises(StateParseError, MolecularTermSymbol, 'X(Π)')

        c2 = MolecularTermSymbol('b(4Π_-3/2)')
        self.assertEqual(c2.irrep, 'Π')
        self.assertEqual(c2.Smult, 4)
        self.assertEqual(c2.term_label, 'b')
        self.assertEqual(c2.J, -1.5)
        #self.assertEqual(c2.html, 'b(<sup>4</sup>Π<sub>-3/2</sub>)')

        c3 = MolecularTermSymbol('A\'(1A1g_0)')
        self.assertEqual(c3.irrep, "A1g")
        self.assertEqual(c3.Smult, 1)
        self.assertEqual(c3.term_label, "A'")
        self.assertEqual(c3.J, 0)
        self.assertEqual(c3.html,'A\'(<sup>1</sup>A<sub>1g</sub><sub>0</sub>)')
        
        c4 = MolecularTermSymbol('1E"1')
        self.assertEqual(c4.html,'<sup>1</sup>E"<sub>1</sub>')
        
        c5 = MolecularTermSymbol('1Σ+u')
        #self.assertEqual(c5.html,'<sup>1</sup>Σ<sup>+</sup><sub>u</sub>')

        c6 = MolecularTermSymbol('1Σ-g')
        #self.assertEqual(c6.html,'<sup>1</sup>Σ<sup>-</sup><sub>g</sub>')
    
    def test_greek_letter_conversion(self):
        m1 = MolecularTermSymbol('1SIGMA-')
        self.assertEqual(m1.Smult, 1)
        self.assertEqual(m1.irrep, 'Σ-')
        self.assertEqual(str(m1), '1Σ-')
           
        m2 = MolecularTermSymbol('2PI')
        self.assertEqual(m2.Smult, 2)
        self.assertEqual(m2.irrep, 'Π')
        self.assertEqual(str(m2), '2Π')
        #self.assertEqual(m2.html, '<sup>2</sup>Π')

        m3 = MolecularTermSymbol('3SIGMA+u')
        self.assertEqual(m3.Smult,3)
        self.assertEqual(m3.irrep,'Σ+u')
        self.assertEqual(str(m3), '3Σ+u')
        #self.assertEqual(m3.html, '<sup>3</sup>Σ<sup>+</sup><sub>u</sub>')

        m3 = MolecularTermSymbol('A(1A")')
        self.assertEqual(str(m3), 'A(1A")')
        #self.assertEqual(m3.html, 'A(<sup>1</sup>A")')

        self.assertRaises(StateParseError, MolecularTermSymbol, 'A(A")')
        self.assertRaises(StateParseError, MolecularTermSymbol, '3B_2A')

if __name__ == '__main__':
    unittest.main()


