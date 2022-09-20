#!/usr/bin/python3
"""
    Module 0-read_file.py
"""


def read_file(filename=""):
    """reads from file and print to stdout"""
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end='')
