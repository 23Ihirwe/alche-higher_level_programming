#!/usr/bin/python3
"""
This module contains a function that returns the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        list: A list of attributes and methods.
    """
    return dir(obj)
