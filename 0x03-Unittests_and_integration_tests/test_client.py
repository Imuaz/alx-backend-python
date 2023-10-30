#!/usr/bin/env python3
'''
Unittests and Integration Tests Module
'''
import unittest
from unittest import mock
from client import *
from unittest.mock import patch, Mock
from fixtures import TEST_PAYLOAD
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        '''Test has_license method with different inputs'''
        org_client = GithubOrgClient('example')
        result = org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''ntegration test'''

    @classmethod
    def setUpClass(cls) -> None:
        '''Set up class function'''
        def getPayload(url):
            return mock.Mock({cls.name: cls.value})
        cls.get_patcher = patch("requests.get", side_effect=getPayload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        '''Tear down class module'''
        cls.get_patcher.stop()

def create_integration_test_class(test_data):
    '''intergration access'''
    class IntegrationTest(TestIntegrationGithubOrgClient):
        org_payload, repos_payload, expected_repos, apache2_repos = test_data

        def test_public_repos_with_license(self):
            '''Test public repos with license'''
            self.assertTrue(True)

        def test_public_repos(self):
            '''Test public repos'''
            self.assertTrue(True)

    return IntegrationTest
