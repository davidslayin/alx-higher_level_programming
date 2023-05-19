#!/usr/bin/python3
"""Defines a square with size"""


class Square:
    """this is a class that defines a square"""
    def __init__(self, size=0):
        """initializing with verification of type"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
