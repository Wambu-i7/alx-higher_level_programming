#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):

    """
    Returns a list containing the names of attributes and methods.
    Parameters:
    - obj: Any object for which you want to retrieve attributes and methods.

    Returns:
    A list of strings representing the names of attributes and methods.
    """
    return (dir(obj))
