#!/usr/bin/env python3
"""
This module has TestAccessNestedMap.
"""
import unittest
from utils import (
        access_nested_map,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the utilis methods.
    """
    @parameterized.expand([
             ({"a": 1}, ("a",), 1),
             ({"a": {"b": 2}}, ("a",), {"b": 2}),
             ({"a": {"b": 2}}, ("a", "b"), 2),
    )]
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map with various nested maps and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)