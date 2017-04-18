"""Unit Tests for DS python-workshop/day2."""


from __future__ import division
import unittest as unittest
from src import substring


class TestSubstring(unittest.TestCase):

    def run_substring(self, func):
        words = ['elephant', 'lion', 'giraffe', 'zebra']
        substrings = ['ion', 'pig', 'eta', 'raz', 'lep']
        result = func(words, substrings)
        expected = ['ion', 'lep']
        self.assertIsInstance(result, list)
        self.assertEqual(set(result), set(expected))

    def test_subtring_old(self):
        self.run_substring(substring.substring_old)

    def test_subtring_new(self):
        self.run_substring(substring.substring_new)


if __name__ == '__main__':
    unittest.main()
