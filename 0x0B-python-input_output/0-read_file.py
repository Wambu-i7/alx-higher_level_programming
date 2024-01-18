#!/usr/bin/python3

"""This function reads a file and prints itto stdout"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as rfile:
        print(rfile.read())
