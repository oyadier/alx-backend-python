#!/usr/bin/env python3
"""A Module to test some funtions in the util file"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test access to nested map
        Args:
            input(map): a nested map
            path(any): a key to the nested map
            output(any): an exptected output of the test
    """
    @parameterized.expand(
        [({"a": 1, }, "a", 1),
         ({"a": {"b": 2}}, "a", {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2)]
        )
    def test_access_nested_map(self, input, path, output):
        self.assertEqual(access_nested_map(input, path), output)

    @parameterized.expand(
        [({}, "a", ),
         ({"a": 1, }, ("a", "b"), )]
        )
    def test_access_nested_map_exception(self, input, path):
        with self.assertRaises(KeyError):
            access_nested_map(input, path)
