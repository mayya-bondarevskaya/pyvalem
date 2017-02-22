# test_atomic_term_symbols.py
# Unit tests for the atomic term symbols module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..atomic_term_symbol import AtomicTermSymbol

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
        self.assertRaises(StateParseError, AtomicTermSymbol, '1PZ')


if __name__ == '__main__':
    unittest.main()

