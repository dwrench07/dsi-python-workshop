"""Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make point`
"""
from __future__ import division
import unittest as unittest

from day3.src.point import Point, Triangle


class TestPoint(unittest.TestCase):

    def test_repr(self):
        p = Point(6, 2)
        answer = 'Point: 6, 2'
        actual = repr(p)
        self.assertEqual(actual, answer)

    def test_length(self):
        p = Point(3, 4)
        answer = 5.0
        actual = p.length()
        self.assertAlmostEqual(actual, answer, actual)

    def test_eq(self):
        p1 = Point(6, 2)
        p2 = Point(6, 2)
        p3 = Point(6, 3)
        self.assertEqual(p2, p1)
        self.assertNotEqual(p3, p1)

    def test_add(self):
        p1 = Point(2, 5)
        p2 = Point(6, 7)
        actual = p1 + p2
        self.assertEqual(actual.x, 8)
        self.assertEqual(actual.y, 12)

    def test_sub(self):
        p1 = Point(2, 5)
        p2 = Point(6, 7)
        actual = p2 - p1
        self.assertEqual(actual.x, 4)
        self.assertEqual(actual.y, 2)

    def test_mul(self):
        p1 = Point(2, 5)
        actual = p1 * 3
        self.assertEqual(actual.x, 6)
        self.assertEqual(actual.y, 15)

    def test_dist(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        actual = p1.dist(p2)
        answer = 5.0
        self.assertAlmostEqual(actual, answer)


class TestTriangle(unittest.TestCase):
    def test_perimeter(self):
        t = Triangle((1, 1), (1, 2), (3, 5))
        a = Point(1, 1).length()
        b = Point(1, 2).length()
        c = Point(3, 5).length()
        answer = a + b + c / 2
        actual = t.perimeter()
        self.assertAlmostEqual(actual, answer)

    def test_area(self):
        t = Triangle((1, 1), (1, 2), (3, 5))
        s = t[0].dist(t[1])
        answer = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        actual = t.area()
        self.assertAlmostEqual(actual, answer)

if __name__ == '__main__':
    unittest.main()
