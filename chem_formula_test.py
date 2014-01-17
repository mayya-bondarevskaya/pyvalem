#! -*- coding: utf-8 -*-
# chem_formula_test.py
# Version 1.0b
# Unit tests for the ChemFormula class.
#
# Copyright (C) 2012-2014 Christian Hill
# Department of Physics and Astronomy, University College London
# christian.hill@ucl.ac.uk
# http://christianhill.co.uk/projects/pyvalem
#
# The support of the Atomic and Molecular Data Unit of the IAEA,
# the Data Center for Plasma Properties at the Korean National Fusion
# Research Institute and the Virtual Atomic and Molecular Data Centre
# during the development of this library is gratefully acknowledged.
#
# This file is part of PyValem
#
# PyValem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyValem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyValem.  If not, see <http://www.gnu.org/licenses/>

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
