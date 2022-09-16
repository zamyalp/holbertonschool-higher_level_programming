#!/usr/bin/python3
"""Module 4-inherits_from.
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
        """Determines if obj is an instance of a class that inherited from a_class"""
    if type(obj) is a_class:
        return Flase
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
