#!/usr/bin/python3
"""
BaseGeometry module
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # must be an integer (bool is NOT accepted)
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # must be greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
