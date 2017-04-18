#!/usr/bin/env python
"""Point and Triangle classes.

This module contains classes to represent points and triangles in
two-dimensional space.
"""

from math import sqrt


class Point(object):
    """Represent a point in 2-dimensional space using x and y cooridnates."""

    def __init__(self, x, y):
        """Initialize a Point with the given x and y coordinate values.

        Parameters
        ----------
        x : float
        y : float
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """Return a string representation of the current Point.

        Examples
        --------
        >>> repr(Point(7, 7))
        "Point(7, 7)"
        """
        pass

    def __eq__(self, other):
        """Return True if the coordinates of self and other are identical.

        Parameters
        ----------
        other : Point

        Examples
        --------
        >>> Point(1, 1) == Point(1, 1)
        True
        >>> Point(1, 1) == Point(3, -1)
        False
        """
        pass

    def __add__(self, other):
        """Return a new Point representing the sum of self and other.

        Parameters
        ----------
        other : Point

        Examples
        --------
        >>> Point(1, 1) + Point(2, 3)
        Point(3, 4)
        >>> Point(1, 1) + Point(-1, -1)
        Point(0, 0)
        """
        pass

    def __sub__(self, other):
        """Return a new Point representing the difference of self and other.

        Parameters
        ----------
        other : Point

        Examples
        --------
        >>> Point(1, 1) - Point(2, 3)
        Point(-1, -2)
        >>> Point(1, 1) - Point(-1, -1)
        Point(2, 2)
        """
        pass

    def __mul__(self, scale_factor):
        """Return a new Point with coordinates multiplied by scale_factor.

        Returns
        -------
        length : float

        Examples
        --------
        >>> Point(1, 1) * 2
        Point(2, 2)
        >>> Point(-3, 5) * 3
        Point(-9, 15)
        >>> Point(-2, 4) * -1
        Point(2, -4)
        """

    def length(self):
        """Return the length of the vector from the origin to this Point.

        Use the Pythagorean Theorem.

        Returns
        -------
        length : float

        Examples
        --------
        >>> length(Point(3,4))
        5
        """

    def dist(self, other):
        """Return the distance between this point and the other point given.

        Use __sub__ and length to compute the distance.

        Parameters
        ----------
        other : Point

        Returns
        -------
        distance : float

        Examples
        --------
        >>> dist(Point(1,1), Point(4, 5))
        5
        """
        pass


class Triangle(object):
    """Represent a triangle in 2-dimensional space using three Points."""

    def __init__(self, vertices):
        """Create a new Triangle with vertices (v1, v2, v3)."""
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        pass
