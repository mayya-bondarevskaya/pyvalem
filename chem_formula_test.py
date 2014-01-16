#! -*- coding: utf-8 -*-
# chem_formula_test.py
import unittest
from chem_formula import ChemFormula
from good_formulas import good_formulas

class GoodFormulas(unittest.TestCase):

    def test_good_formulas(self):
        for ordinary_formula in good_formulas:
            sf = good_formulas[ordinary_formula]['stoichiometric_formula']
            html = good_formulas[ordinary_formula]['html']
            slug = good_formulas[ordinary_formula].get('slug')
            rmm = good_formulas[ordinary_formula]['rmm']

            pf = ChemFormula(ordinary_formula)
            self.assertEqual(sf,pf.stoichiometric_formula())
            self.assertEqual(html, pf.html)
            if slug:
                self.assertEqual(slug, pf.slug)
            self.assertTrue(abs(rmm - pf.rmm) < 1.e-8)

if __name__ == "__main__":
    unittest.main()
