#!/usr/bin/python3
"""Defines a function that checks if a class is an inherited class."""


def inherits_from(obj, a_class):

    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from the
    specified class; otherwise False.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    True if obj is an instance that inherited from
    a_class; otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
