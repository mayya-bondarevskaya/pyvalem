# test_racah_symbols.py
# Unit tests for the key-value pair states module of PyValem
#
# Copyright (C) 2012-2017 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..racah_symbol import RacahSymbol

class RacahSymbolTest(unittest.TestCase):
    def test_racah_symbol(self):

        # The RacahSymbol class is just a stub at the moment, so
        # it doesn't extend the functionality of the base State class at all.
        rs1 = RacahSymbol('Absolutely anything at all')
        self.assertEqual(str(rs1), 'Absolutely anything at all')
        self.assertEqual(rs1.html, 'Absolutely anything at all')

        # When it has been written, this sort of thing is what a RacahSymbol
        # looks like.
        rs2 = RacahSymbol('3d[3/2]_2')
        self.assertEqual(str(rs2), '3d[3/2]_2')
        self.assertEqual(rs2.html, '3d[3/2]_2')

if __name__ == '__main__':
    unittest.main()


