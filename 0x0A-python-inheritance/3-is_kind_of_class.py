#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):

    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from the
    specified class; otherwise False.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    True if obj is an instance of a_class or any subclass
    of a_class; otherwise False.
    """

    return isinstance(obj, a_class)
