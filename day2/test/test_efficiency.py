"""Unit Tests for DS python-workshop/day2."""


from __future__ import division
import unittest as unittest
from collections import Counter
from src import efficiency


class TestEfficiency(unittest.TestCase):

    def test_find_invalid_words(self):
        words = ['a', 'b', 'c']
        answer = ['d', 'd', 'e']
        actual = efficiency.find_invalid_words(words, 'data/tiny.txt')
        self.assertIsInstance(actual, list)
        self.assertEqual(Counter(actual), Counter(answer))

    def test_find_common_characters(self):
        s = 'abcaabbdad'
        num = 2
        answer = ['a', 'b']
        actual = efficiency.find_common_characters(s, num)
        self.assertIsInstance(actual, list)
        self.assertEqual(sorted(actual), sorted(answer))

    def test_sum_to_zero(self):
        lst = [9, 4, -5, 8, -4, 7, 3]
        answer = (-4, 4)
        actual = efficiency.sum_to_zero(lst)
        self.assertIsInstance(actual, tuple)
        self.assertEqual(set(actual), set(answer))


if __name__ == '__main__':
    unittest.main()
