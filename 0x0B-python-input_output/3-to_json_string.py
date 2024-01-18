#!/usr/bin/python3
"""This module provides methods for working with json"""
import json

"""This function returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """
    Serializes the object(string) to json representation.

    Parameters:
        -Object- the object to be serialized.

    Returns:
        -The json representation of the object.
    """
    json_string = json.dumps(my_obj)
    return json_string
