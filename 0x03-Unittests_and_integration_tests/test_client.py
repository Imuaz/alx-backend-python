#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from unittest import mock
from client import *
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''class for github.org client'''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', new_callable=Mock)
    def test_org(self, input, mock_get_json):
        '''test for an expected result'''
        GithubOrgClient.ORG_URL = input
        org_client = GithubOrgClient(input)
        org_client.org()

    @patch('client.GithubOrgClient._public_repos_url', return_value='github.com')
    def test_public_repos_url(self, mock_method):
        '''Test public repositorys  url'''
        self.assertEqual(GithubOrgClient._public_repos_url, mock_method)

    @patch('client.GithubOrgClient.public_repos', return_value='github.com')
    def test_public_repos(self, mock_method):
        '''Tests public repository'''
        result = GithubOrgClient.public_repos()
        self.assertEqual(result, 'github.com')
        mock_method.assert_called_once()
