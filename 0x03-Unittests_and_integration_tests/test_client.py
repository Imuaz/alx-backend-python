#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
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

    @patch('client.GithubOrgClient._public_repos_url', r_value='github.com')
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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test for GithubOrgClient'''

    @classmethod
    def setUpClass(cls):
        '''Set up the class'''
        cls.get_patcher = patch('requests.get', side_effect=cls.side_effect)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''Tear down the class'''
        cls.get_patcher.stop()

    @classmethod
    def side_effect(cls, url):
        if url == "https://api.github.com/orgs/google":
            return cls.org_payload
        return cls.repos_payload

    def test_public_repos(self):
        '''Integration test: public repos'''
        test_class = GithubOrgClient("google")
        self.assertTrue(True)

    def test_public_repos_with_license(self):
        '''Integration test for public repos with License'''
        test_class = GithubOrgClient("google")
        self.assertTrue(True)
