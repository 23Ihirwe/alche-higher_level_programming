#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if obj is an inherited instance (not the class itself)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
