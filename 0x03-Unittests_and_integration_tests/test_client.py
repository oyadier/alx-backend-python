#!/usr/bin/env python3
"""A Test file for HTTP calls"""
import unittest
from unittest.mock import PropertyMock, patch
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

    def test_public_repos_url(self):
        """ Test the urls
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
            
    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        List all the pay repos in an expected paayo===
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()
        
    