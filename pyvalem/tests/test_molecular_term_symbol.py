from ..molecular_term_symbol import MolecularTermSymbol
from ..state import State, StateParseError
import unittest

class MolecularTermSymbolTest(unittest.TestCase):
    def test_greek_letter_conversion(self):
        m1 = MolecularTermSymbol('1SIGMA-')
        self.assertEqual(m1.Smult, 1)
        self.assertEqual(m1.irrep, 'Σ-')
        self.assertEqual(str(m1), '1Σ-')
           
        m2 = MolecularTermSymbol('2PI')
        self.assertEqual(m2.Smult, 2)
        self.assertEqual(m2.irrep, 'Π')
        self.assertEqual(str(m2), '2Π')
        self.assertEqual(m2.html, '<sup>2</sup>Π')

        m3 = MolecularTermSymbol('3SIGMA+u')
        self.assertEqual(m3.Smult,3)
        self.assertEqual(m3.irrep,'Σ+u')
        self.assertEqual(str(m3), '3Σ+u')
        self.assertEqual(m3.html, '<sup>3</sup>Σ<sup>+</sup><sub>u</sub>')

        m3 = MolecularTermSymbol('A(1A")')
        self.assertEqual(str(m3), 'A(1A")')
        self.assertEqual(m3.html, 'A(<sup>1</sup>A")')

        self.assertRaises(StateParseError, MolecularTermSymbol, 'A(A")')
        self.assertRaises(StateParseError, MolecularTermSymbol, '3B_2A')

    
if __name__ == '__main__':
    unittest.main()
