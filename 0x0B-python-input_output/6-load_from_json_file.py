#!/usr/bin/python3
"""
    Module 6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """creates object from a JSON file"""
    with open(filename, encoding="UTF8") as f:
        return json.loads(f.read())
