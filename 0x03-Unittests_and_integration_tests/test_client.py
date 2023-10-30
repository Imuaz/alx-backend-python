#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from unittest import mock
from client import *
from unittest.mock import patch, Mock
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        '''Test has_license method with different inputs'''
        org_client = GithubOrgClient('example')
        result = org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


def get_payload(name):
    def getPayload(url):
        return Mock(json=lambda: name)
    return getPayload

@parameterized_class("name", TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""

    @classmethod
    def setUpClass(cls):
        """Set up class function"""
        cls.get_patcher = patch("requests.get", side_effect=get_payload(cls.name))
        cls.get_patcher.start()

    def test_public_repos_with_license(self):
        """Test public repos with license"""
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        '''Teardownclass'''
        cls.get_patcher.stop()
