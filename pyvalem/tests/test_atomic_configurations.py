# test_atomic_configurations.py
# Unit tests for the atomic configuration module of PyValem
#
# Copyright (C) 2012-2016 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..atomic_configuration import AtomicConfiguration,AtomicConfigurationError


class AtomicConfigurationTest(unittest.TestCase):

    def test_atomic_configuration(self):
        c4 = AtomicConfiguration('[He].2s1')

        c0 = AtomicConfiguration('1s2')
        c1 = AtomicConfiguration('1s2.2s2')
        c2 = AtomicConfiguration('1s2.2s2.2p6')
        c3 = AtomicConfiguration('1s2.2s2.2p6.3s2.3d10')
        self.assertRaises(StateParseError, AtomicConfiguration, 's4.w2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s 2.2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2. 2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2 2s2 2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, 'He.2s1')
        self.assertRaises(StateParseError, AtomicConfiguration, '[Bi].2s1')
        self.assertRaises(StateParseError, AtomicConfiguration, '1ss2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2..2s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2,2s2,2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, '1s2;2s2:2p6')
        self.assertRaises(StateParseError, AtomicConfiguration, '')
        self.assertRaises(StateParseError, AtomicConfiguration, '.1s2')
        self.assertRaises(StateParseError, AtomicConfiguration, '[He].[Ne]')
        self.assertRaises(StateParseError, AtomicConfiguration, '[He]2s1')
        
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.1s2.2s2')
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.2s2.2p7')
        self.assertRaises(AtomicConfigurationError, AtomicConfiguration,
                                                    '1s2.2s2.2d2')
 

if __name__ == '__main__':
    unittest.main()

 
