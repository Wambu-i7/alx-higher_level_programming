#!/usr/bin/python3
"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """Appends contents on a text file and returns numberof characters
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='a', encoding='utf-8') as rfile:
        return rfile.write(text)
