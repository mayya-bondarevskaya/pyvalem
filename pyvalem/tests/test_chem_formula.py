# test_chem_formula.py
# Unit tests for the chem_formula module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

from ..chem_formula import ChemFormula
from .good_formulas import good_formulas
import unittest

class ChemFormulaTest(unittest.TestCase):

    def test_stoichiometric_formula_test(self):
        cf = ChemFormula('C2F4H2')
        self.assertEqual(cf.stoichiometric_formula(), 'H2C2F4')
        self.assertEqual(cf.stoichiometric_formula('alphabetical'), 'C2F4H2')
        self.assertEqual(cf.stoichiometric_formula('hill'), 'C2H2F4')

    def test_html_and_slug(self):
        f = (('NO+', 'NO+', 'NO<sup>+</sup>', 'NO_p'),
             ('OH-', 'HO-', 'OH<sup>-</sup>', 'OH_m'),
             ('CoN6H18-2', 'H18N6Co-2',
              'CoN<sub>6</sub>H<sub>18</sub><sup>2-</sup>',
              'CoN6H18_m2'),
             ('(14N)(1H)(16O)2(18O)(16O)', '(1H)(14N)(16O)3(18O)',
              '<sup>14</sup>N<sup>1</sup>H<sup>16</sup>O<sub>2</sub>'
                      '<sup>18</sup>O<sup>16</sup>O',
              '14N-1H-16O2-18O-16O')
             )

        for formula, stoich_formula, html, slug in f:
            cf = ChemFormula(formula)
            self.assertEqual(cf.stoichiometric_formula(), stoich_formula)
            self.assertEqual(cf.html, html)
            self.assertEqual(cf.slug, slug)

    def test_moieties(self):
        cf = ChemFormula('H2NC(CH3)2CO2H')
        self.assertEqual(cf.html, 'H<sub>2</sub>NC(CH<sub>3</sub>)'
                                  '<sub>2</sub>CO<sub>2</sub>H')
        self.assertEqual(cf.slug, 'H2NC_d__CH3_d__2CO2H')
        self.assertEqual(cf.atoms, {'H', 'C', 'N', 'O'})

    def test_good_formulas(self):
        for formula in good_formulas:
            cf = ChemFormula(formula)
            #print(formula)
            self.assertEqual(cf.stoichiometric_formula(),
                             good_formulas[formula]['stoichiometric_formula'])
            self.assertEqual(cf.html, good_formulas[formula]['html'])
            self.assertEqual(cf.slug, good_formulas[formula]['slug'])
            self.assertAlmostEqual(cf.rmm, good_formulas[formula]['rmm'])
            if 'natoms' in good_formulas[formula].keys():
                self.assertEqual(cf.natoms, good_formulas[formula]['natoms'])
            if 'latex' in good_formulas[formula].keys():
                self.assertEqual(cf.latex, good_formulas[formula]['latex']) 

    def test_M(self):
        cf = ChemFormula('M')
        self.assertEqual(cf.stoichiometric_formula(), 'M')
        self.assertEqual(cf.html, 'M')
        self.assertEqual(cf.slug, 'M')
        self.assertIsNone(cf.rmm)
        self.assertIsNone(cf.natoms)
        self.assertIsNone(cf.charge)
        self.assertEqual(cf.atoms, {'M'})

    def test_e(self):
        cf = ChemFormula('e-')
        self.assertEqual(cf.stoichiometric_formula(), 'e-')
        self.assertEqual(cf.html, 'e<sup>-</sup>')
        self.assertEqual(cf.slug, 'e_m')
        self.assertEqual(cf.rmm, 5.48579909e-04)
        self.assertIsNone(cf.natoms)
        self.assertEqual(cf.charge, -1)
        
    def test_photon(self):
        for cf in (ChemFormula('hν'), ChemFormula('hv')):
            self.assertEqual(cf.stoichiometric_formula(), 'hν')
            self.assertEqual(cf.slug, 'hv')
            self.assertEqual(cf.html, 'hν')
            self.assertIsNone(cf.rmm)
            self.assertIsNone(cf.natoms)
            self.assertEqual(cf.charge, 0)
        

if __name__ == '__main__':
    unittest.main()
