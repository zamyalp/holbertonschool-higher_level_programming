#!/usr/bin/python3
"""
    Module 2-read_lines.
"""


def append_write(filename="", text=""):
    """Reads and prints lines from filename."""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
