# test_diatomic_molecular_configurations.py
# Unit tests for the diatomic molecular configuration module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..diatomic_molecular_configuration import (DiatomicMolecularConfiguration,
                                          DiatomicMolecularConfigurationError)


class DiatomicMolecularConfigurationTest(unittest.TestCase):

    def test_diatomic_molecular_configuration(self):
        c1 = DiatomicMolecularConfiguration('1σ')
        self.assertEqual(c1.html, '1σ<sub>1<\sub>')
        
        c2 = DiatomicMolecularConfiguration('1σ2')
        self.assertEqual(c2.html, '1σ<sub>2<\sub>')
        
        c3 = DiatomicMolecularConfiguration('1σg2')
        self.assertEqual(c3.html, '1σg<sub>2<\sub>')
        
        c4 = DiatomicMolecularConfiguration('1σu2')
        self.assertEqual(c4.html, '1σu<sub>2<\sub>')
        
        c5 = DiatomicMolecularConfiguration('1sigmau')
        self.assertEqual(c5.html, '1σu<sub>1<\sub>')
        
        c6 = DiatomicMolecularConfiguration('1sigmau2')
        self.assertEqual(c6.html, '1σu<sub>2<\sub>')

        c7 = DiatomicMolecularConfiguration('1sigmau2.2sigmag1')
        self.assertEqual(c7.html, '1σu<sub>2<\sub>.2σg<sub>1<\sub>')

        self.assertRaises(StateParseError, DiatomicMolecularConfiguration,
                          's4.w2')
        
        self.assertRaises(DiatomicMolecularConfigurationError,
                DiatomicMolecularConfiguration, '1σu2.1σu2')
        self.assertRaises(DiatomicMolecularConfigurationError,
                DiatomicMolecularConfiguration, '1sigma3')
        self.assertRaises(DiatomicMolecularConfigurationError,
                DiatomicMolecularConfiguration, '1pi6')
 

if __name__ == '__main__':
    unittest.main()

 

