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
        c2 = DiatomicMolecularConfiguration('1σ2')
        c3 = DiatomicMolecularConfiguration('1σg2')
        c4 = DiatomicMolecularConfiguration('1σu2')
        c5 = DiatomicMolecularConfiguration('1sigmau')
        c6 = DiatomicMolecularConfiguration('1sigmau2')

        c7 = DiatomicMolecularConfiguration('1sigmau2.2sigmag1')

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

 

