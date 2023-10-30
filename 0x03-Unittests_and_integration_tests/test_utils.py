#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import *


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, exception_type):
        '''test for the expected exception raised.'''
        with self.assertRaises(exception_type):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    '''Get json testing class'''

    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])

    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''checks the expected result'''
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)
        
        # Verify that the mocked 'get' method was called exactly once with the test URL
        mock_get.assert_called_once_with(test_url)
        # Verify that the result of 'get_json' is equal to the test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Test to memoized class'''
    def test_memoize(self):
        '''checks wheather correct result is returned'''
        class TestClass:
            ''''test class with a method and a memoized property'''
            def a_method(self):
                '''test method'''
                return 42

            @memoize
            def a_property_memoized(self):
                '''returns a method'''
                return self.a_method()

        # Create an instance of the test class
        test_instance = TestClass()

        # Mock the a_method with a mock object
        with patch.object(test_instance, 'a_method', value=42) as mock_method:
            # Call a_property_memoized twice
            result1 = test_instance.a_property_memoized()
            result2 = test_instance.a_property_memoized()

            # Assert that a_method is called only once
            mock_method.assert_called_once()
