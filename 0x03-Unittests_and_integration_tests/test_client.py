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
    def test_org(self, input):
        with mock.patch('client.get_json') as mock_get_json:
            GithubOrgClient.ORG_URL = input
            org_client = GithubOrgClient(input)
            org_client.org()
            expected_url = f'https://api.github.com/orgs/{input}'
            mock_get_json.assert_called_once_with(expected_url)
