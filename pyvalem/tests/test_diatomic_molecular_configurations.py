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
        c1 = DiatomicMolecularConfiguration('1σ2')
        c1 = DiatomicMolecularConfiguration('1σg2')
        c1 = DiatomicMolecularConfiguration('1σu2')
        c1 = DiatomicMolecularConfiguration('1sigmau')
        c1 = DiatomicMolecularConfiguration('1sigmau2')

        c1 = DiatomicMolecularConfiguration('1sigmau2.2sigmag1')

        self.assertRaises(StateParseError, DiatomicMolecularConfiguration,
                          's4.w2')
        
        self.assertRaises(DiatomicMolecularConfigurationError,
                DiatomicMolecularConfiguration, '1σu2.1σu2')
 

if __name__ == '__main__':
    unittest.main()

 

