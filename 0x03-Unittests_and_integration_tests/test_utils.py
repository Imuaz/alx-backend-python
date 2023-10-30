#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing access nested map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        '''test wheather the method return as expected'''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
