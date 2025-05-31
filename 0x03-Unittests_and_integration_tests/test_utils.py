#!/usr/bin/env python3
"""
Unit tests for functions in the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map function."""

    @parameterized.expand([
        ({"x": 10}, ("x",), 10),
        ({"x": {"y": 20}}, ("x",), {"y": 20}),
        ({"x": {"y": 20}}, ("x", "y"), 20),
    ])
    def test_access_nested_map(self, nested, keys, expected):
        """Test correct output for valid nested keys."""
        self.assertEqual(access_nested_map(nested, keys), expected)

    @parameterized.expand([
        ({}, ("missing",), "missing"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_key_error(self, nested, keys, missing_key):
        """Test KeyError is raised for missing keys."""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested, keys)
        self.assertEqual(str(error.exception), f"'{missing_key}'")


class TestGetJson(unittest.TestCase):
    """Unit tests for get_json function."""

    @parameterized.expand([
        ("https://api.example.com", {"data": 123}),
        ("https://holberton.io", {"status": "ok"}),
    ])
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Test get_json returns expected dictionary from mocked response."""
        mock_resp = Mock()
        mock_resp.json.return_value = payload
        mock_get.return_value = mock_resp

        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoizeDecorator(unittest.TestCase):
    """Unit tests for memoize decorator."""

    def test_memoize_behavior(self):
        """Test memoize caches method result properly."""

        class Sample:
            """Sample class with a method to memoize."""

            def method(self):
                return 100

            @memoize
            def cached(self):
                return self.method()

        obj = Sample()

        with patch.object(Sample, 'method', return_value=100) as mock_method:
            self.assertEqual(obj.cached, 100)
            self.assertEqual(obj.cached, 100)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
