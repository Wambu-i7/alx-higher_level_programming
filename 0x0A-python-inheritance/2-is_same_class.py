#!/usr/bin/python3
"""Defines a function that returns True if the object is exactly
   an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):

    """Checking if the object is an instance of a class
    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
