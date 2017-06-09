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
        rs1 = RacahSymbol('4s[3/2]_2')
        self.assertEqual(rs1.principal, 4)
        self.assertEqual(rs1.orbital, 's')
        self.assertEqual(rs1.parent_rot, 1.5)
        self.assertEqual(rs1.k_num, 3)
        self.assertEqual(rs1.k_den, 2)
        self.assertEqual(rs1.j_term, 2)
        self.assertEqual(rs1.html, '4s[3/2]<sub>2</sub>')

        rs2 = RacahSymbol("4p'[1/2]_0")
        self.assertEqual(rs2.principal, 4)
        self.assertEqual(rs2.orbital, "p'")
        self.assertEqual(rs2.parent_rot, 0.5)
        self.assertEqual(rs2.k_num, 1)
        self.assertEqual(rs2.k_den, 2)
        self.assertEqual(rs2.j_term, 0)
        self.assertEqual(rs2.html, "4p'[1/2]<sub>0</sub>")
        
        rs3 = RacahSymbol("3d'[5/2]_3")
        self.assertEqual(rs3.principal, 3)
        self.assertEqual(rs3.orbital, "d'")
        self.assertEqual(rs3.parent_rot, 0.5)
        self.assertEqual(rs3.k_num, 5)
        self.assertEqual(rs3.k_den, 2)
        self.assertEqual(rs3.j_term, 3)
        self.assertEqual(rs3.html, "3d'[5/2]<sub>3</sub>")
        
        rs4 = RacahSymbol("5s'[1/2]_1")
        self.assertEqual(rs4.principal, 5)
        self.assertEqual(rs4.orbital, "s'")
        self.assertEqual(rs4.parent_rot, 0.5)
        self.assertEqual(rs4.k_num, 1)
        self.assertEqual(rs4.k_den, 2)
        self.assertEqual(rs4.j_term, 1)
        self.assertEqual(rs4.html, "5s'[1/2]<sub>1</sub>")
        
if __name__ == '__main__':
    unittest.main()


