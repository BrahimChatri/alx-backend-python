#!/usr/bin/env python3
"""
Unit and integration tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures  # Make sure fixtures.py exists and contains expected attributes


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org property returns correct data"""
        expected = {"login": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """Test _public_repos_url returns the correct repos_url"""
        client = GithubOrgClient("test_org")
        payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns list of repo names"""
        client = GithubOrgClient("test_org")
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}}
        ]

        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "fake_url"
            repos = client.public_repos()

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("fake_url")
            self.assertEqual(repos, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns correct boolean"""
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Start patcher and setup responses"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def json_side_effect(url, *args, **kwargs):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return {}

        mock_response = unittest.mock.Mock()
        mock_response.json.side_effect = lambda: json_side_effect(
            cls.mock_get.call_args[0][0]
        )
        cls.mock_get.return_value = mock_response

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test all public repos"""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtered repos by license"""
        client = GithubOrgClient("google")
        repos = client.public_repos(license_key="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
