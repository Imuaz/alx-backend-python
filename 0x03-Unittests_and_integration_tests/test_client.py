#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from client import *
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''class for github.org client'''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'login': 'example_org'})
    def test_org(self, org_name, mock_get_json):
        '''test the correct result'''
        org_client = GithubOrgClient(org_name)
        result = org_client.get_org()
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {'login': 'example_org'})

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value=[{'name': 'repo1'}, {'name': 'repo2'}])
    def test_repos_payload(self, org_name, mock_get_json):
        '''test the public repo'''
        org_client = GithubOrgClient(org_name)
        result = org_client.repos_payload()
        expected_url = org_client._public_repos_url
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, [{'name': 'repo1'}, {'name': 'repo2'}])
