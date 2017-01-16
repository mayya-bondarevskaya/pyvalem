from ..molecular_term_symbol import MolecularTermSymbol
from ..state import State, StateParseError
import unittest

class MolecularTermSymbolTest(unittest.TestCase):
    def test_greek_letter_conversion(self):
        m1 = MolecularTermSymbol('1SIGMA-')
        self.assertEqual(m1.Smult,1)
        self.assertEqual(m1.irrep,'Σ-')
           
        m2 = MolecularTermSymbol('3SIGMA+u')
        self.assertEqual(m2.Smult,3)
        self.assertEqual(m2.irrep,'Σ+u')
    
if __name__ == '__main__':
    unittest.main()