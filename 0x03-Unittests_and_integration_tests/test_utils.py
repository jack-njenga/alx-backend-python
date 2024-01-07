#!/usr/bin/env python3
"""
write the first unit test for utils.access_nested_map.
"""
import unittest
import utils
from parameterized import parameterized
from typing import Union, Dict, Mapping, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests that the method returns what it is supposed to.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Union[Dict, int]],
                               path: Tuple[str],
                               result: Union[Dict, int]) -> None:
        """Access test"""
        self.assertEqual(utils.access_nested_map(nested_map, path), result)
