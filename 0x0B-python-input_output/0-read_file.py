#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """ Reads the content of a text file (UTF-8) and prints it to stdout."""
    with open(filename, mode='r', encoding='utf-8') as rfile:
        print(rfile.read(), end="")
