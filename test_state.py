# test_state.py
# Unit tests for the state module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

from state import AtomicTermSymbol
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

if __name__ == '__main__':
    unittest.main()
