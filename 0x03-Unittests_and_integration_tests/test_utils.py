#!/usr/bin/env python3
"""A Module to test some funtions in the util file"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import MagicMock, patch
from utils import get_json


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

    @patch('utils.requests.get')
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, input, output, mock_requests):
        response = MagicMock()
        response.json.return_value = output
        mock_requests.return_value = response

        result = get_json(input)
        mock_requests.assert_called_once_with(result)
        self.assertEqual(result, output)
