# test_key_value_pairs.py
# Unit tests for the key-value pair states module of PyValem
#
# Copyright (C) 2012-2017 Christian Hill
#
# This file is part of PyValem

import unittest

from ..state import StateParseError
from ..key_value_pair import KeyValuePair

class KeyValuePairTest(unittest.TestCase):

    def test_key_value_pair(self):
        kv1 = KeyValuePair('n=1')
        self.assertEqual(kv1.key, 'n')
        self.assertEqual(kv1.value, '1')
        self.assertEqual(str(kv1), 'n=1')
        self.assertEqual(kv1.html, 'n=1')

        kv2 = KeyValuePair('C = 45a#')
        self.assertEqual(kv2.key, 'C')
        self.assertEqual(kv2.value, '45a#')
        self.assertEqual(str(kv2), 'C=45a#')
        self.assertEqual(kv2.html, 'C=45a#')

        self.assertRaises(StateParseError, KeyValuePair, '*')

if __name__ == '__main__':
    unittest.main()

