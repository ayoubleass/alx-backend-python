#!/usr/bin/env python3
"""
This module has TestAccessNestedMap.
"""
from parameterized import parameterized
import unittest
import utils
from unittest.mock import patch, Mock
from utils import (
        access_nested_map,
        get_json
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the utilis methods.
    """
    @parameterized.expand([
             ({"a": 1}, ("a",), 1),
             ({"a": {"b": 2}}, ("a",), {"b": 2}),
             ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map with various nested maps and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a"), "a"),
            ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test the access_nested_map error handling.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(
                "KeyError('{}')".format(expected), repr(error.exception))


class TestGetJson(unittest.TestCase):
    """
    Test the utilis method getjson.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that utils.get_json returns the expected result.
        """
        res = Mock()
        res.json.return_value = test_payload
        mock_get.return_value = res
        result = utils.get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test the utils.memoize method.
    """
    def test_memoize(self):
        """
        Test memoize method.
        """


        class TestClass:
            """
            wrapper class for memoize method.
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
