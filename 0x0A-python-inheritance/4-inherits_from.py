#!/usr/bin/python3
"""Module 4-inherits_from.
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """
   Returns true or false
    """
    return issubclass(type(obj), a_class) and type(obj) !=a_class
