#!/usr/bin/env python3
"""A Test file for HTTP calls"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Making a network call test"""
    @parameterized.expand([
            ('google'),('abc')
        ])
    @patch('client.get_son')
    def test_org(self, input, output):
      """ Testing that Git... returs a correct value"""
      test_class = GithubOrgClient(input)
      test_class.org()
      output.assert_called_once_with(f'https://api.github.com/orgs/{input}')