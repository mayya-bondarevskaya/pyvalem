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
from ..vibrational_state import VibrationalState
import unittest

class VibrationalTermSymbolTest(unittest.TestCase):
    def test_vibrational_term_symbol(self):
        e0 = VibrationalState('1/2')
        self.assertEqual(e0.J,0.5)
        
        self.assertRaises(StateParseError, VibrationalState, '1/5')
        #self.assertRaises(StateParseError, VibrationalState, '1\5') NEEDS RESOLVING

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
        c0 = MolecularTermSymbol('X(3Π)')
        self.assertEqual(c0.Smult, 3)
        self.assertEqual(c0.irrep, 'Π')
        self.assertEqual(c0.term_label, 'X')
        self.assertEqual(c0.html, 'X(<sup>3</sup>Π)')

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
        self.assertEqual(c2.html, 'b(<sup>4</sup>Π<sub>-3/2</sub>)')

        c3 = MolecularTermSymbol('A\'(1A1g_0)')
        self.assertEqual(c3.irrep, "A1g")
        self.assertEqual(c3.Smult, 1)
        self.assertEqual(c3.term_label, "A'")
        self.assertEqual(c3.J, 0)
        self.assertEqual(c3.html,'A\'(<sup>1</sup>A<sub>1g</sub><sub>0</sub>)')
        
        c4 = MolecularTermSymbol('1E"1')
        self.assertEqual(c4.html,'<sup>1</sup>E"<sub>1</sub>')
        
        c5 = MolecularTermSymbol('1Σ+u')
        self.assertEqual(c5.html,'<sup>1</sup>Σ<sup>+</sup><sub>u</sub>')

        c6 = MolecularTermSymbol('1Σ-g')
        self.assertEqual(c6.html,'<sup>1</sup>Σ<sup>-</sup><sub>g</sub>')
if __name__ == '__main__':
    unittest.main()
