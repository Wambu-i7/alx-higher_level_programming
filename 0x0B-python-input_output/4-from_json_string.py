#!/usr/bin/python3
"""This module provides methods for working with json"""
import json

"""This function returns an object(python data structure)"""


def from_json_string(my_str):
    """
    Deserializes the string to python data structure.

    Parameters:
        -String- the string to be deserialized.

    Returns:
        -Python data structure.
    """
    python_object = json.loads(my_str)
    return python_object
