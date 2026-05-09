#!/usr/bin/python3
"""Module for BaseGeometry with area method."""


class BaseGeometry:
    """Base class for geometry with public instance method."""

    def area(self):
        """Raises an Exception as area is not implemented."""
        raise Exception("area() is not implemented")
