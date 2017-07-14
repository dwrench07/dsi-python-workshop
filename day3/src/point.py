#!/usr/bin/env python
"""Point and Triangle classes.

This module contains classes to represent points and triangles in
two-dimensional space.
"""
from itertools import combinations
from math import sqrt


class Point:
    """Represent a point in 2-dimensional space using x and y cooridnates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point: {self.x}, {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scale_factor):
        return Point(self.x * factor, self.y * factor)

    def length(self):
        """Return the length of the vector from the origin to this Point.

        Use the Pythagorean Theorem. a**2 + b**2 == c**2

        Returns
        -------
        length : float

        Examples
        --------
        >>> length(Point(3, 4))
        5
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def dist(self, other):
        return (self - other).length()


class Triangle:
    def __init__(self, a, b, c):
        if not isinstance(a, Point):
            raise TypeError('Triangle object takes 3 Points')
        self.a = a
        self.b = b
        self.c = c
        if not self.area():
            raise Exception('3 points for triangle in a line')

    def area(self):
        a, b, c = self.a, self.b, self.c
        return abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2.

    def perimeter(self):
        a, b, c = self.a, self.b, self.c
        return a.dist(b) + b.dist(c) + c.dist(a)


if __name__ == '__main__':
