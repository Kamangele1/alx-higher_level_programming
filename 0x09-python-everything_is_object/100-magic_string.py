#!/usr/bin/python3
def magic_string():
    magic_string.x = get attr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.x -1) + "BestSchool")

