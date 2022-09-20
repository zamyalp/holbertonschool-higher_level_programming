#!/usr/bin/python3
""" Module 1-write_file """


def write_file(filename="", text=""):
    """Will write to a text file and return the number of characters"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
