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

        # Ensure that get_json is not executed
        mock_get_json.assert_not_called()
