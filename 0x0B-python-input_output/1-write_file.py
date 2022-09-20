#!/usr/bin/python3
""" Module 1-write_file """



def write_file(filename="", text=""):
    """counts lines in filename."""
    with open(filename, mode='w', encoding="UTF8") as f:
        return f.write(text)
