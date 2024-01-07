#!/usr/bin/env python3
"""
write the first unit test for utils.access_nested_map.
"""
import unittest
import utils
from utils import memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests that the method returns what it is supposed to.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Access test"""
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, e):
        """Exception raise test"""
        with self.assertRaises(e):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests that utils.get_json returns the expected result.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """json test"""
        kwargs = {'json.return_value': payload}
        with patch('requests.get', return_value=Mock(**kwargs)) as mocked:
            self.assertEqual(utils.get_json(url), payload)
            mocked.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """memoize test"""

    def test_memoize(self):
        """memoize test"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mocked.assert_called_once()
