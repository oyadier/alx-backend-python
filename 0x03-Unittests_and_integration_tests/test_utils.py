#!/usr/bin/env python3
"""A Module to test some funtions in the util file"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import (access_nested_map, get_json, memoize)
from typing import Dict


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


class TestGetJson(unittest.TestCase):
    """Make a Mock Http calss"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_get) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Memoization"""
    def test_memoize(self):
        """A memoization Class"""
        class TestClass:
            """Inward memoization"""
            def a_method(self):
                """Returning the same result"""
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
