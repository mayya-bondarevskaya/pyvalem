# test_state.py
# Unit tests for the state module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

from ..state import StateParseError
from ..atomic_term_symbol import AtomicTermSymbol
from ..atomic_configuration import AtomicConfiguration,AtomicConfigurationError
from ..molecular_term_symbol import MolecularTermSymbol
import unittest

class AtomicTermSymbolTest(unittest.TestCase):

    def test_atomic_term_symbol(self):
        a0 = AtomicTermSymbol('3P_1/2')
        self.assertEqual(a0.html, '<sup>3</sup>P<sub>1/2</sub>')
        # The quantum numbers: NB since these are half-integral, they can
        # be tested with assertEqual instead of assertAlmostEqual
        self.assertEqual(a0.S, 1.)
        self.assertEqual(a0.L, 1)
        self.assertEqual(a0.J, 0.5)

        a1 = AtomicTermSymbol('4D')
        self.assertEqual(a1.html, '<sup>4</sup>D')
        self.assertEqual(a1.S, 1.5)
        self.assertEqual(a1.L, 2)
        self.assertIsNone(a1.J)

        a2 = AtomicTermSymbol('2Po_1/2')
        self.assertEqual(a2.html, '<sup>2</sup>P<sup>o</sup><sub>1/2</sub>')
        self.assertEqual(a2.parity, 'o')
        self.assertEqual(a2.L, 1)

        self.assertRaises(StateParseError, AtomicTermSymbol, '1P_0')

class AtomicConfigurationTest(unittest.TestCase):

    def test_atomic_configuration(self):
        c4 = AtomicConfiguration('[He].2s1')

        c0 = AtomicConfiguration('1s2')
        c1 = AtomicConfiguration('1s2.2s2')
        c2 = AtomicConfiguration('1s2.2s2.2p6')
        c3 = AtomicConfiguration('1s2.2s2.2p6.3s2.3d10')
        self.assertRaises(StateParseError, AtomicConfiguration, 's4.w2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s 2.2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2. 2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2 2s2 2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, 'He.2s1')
        self.assertRaises(StateParseError, AtomicConfiguration, '[Bi].2s1')
        self.assertRaises(StateParseError, AtomicConfiguration, '1ss2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2..2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2,2s2,2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2;2s2:2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, '')
        self.assertRaises(StateParseError, AtomicConfiguration, '.1s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '[He].[Ne]')
        self.assertRaises(StateParseError, AtomicConfiguration, '[He]2s1')
        
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.1s2.2s2')
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.2s2.2p7')
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.2s2.2d2')
 

class MolecularTermSymbolTest(unittest.TestCase):

    def test_molecular_term_symbol(self):
        c0 = MolecularTermSymbol('X(4Π)')
        self.assertRaises(StateParseError, MolecularTermSymbol, 'X(Π)')

if __name__ == '__main__':
    unittest.main()
