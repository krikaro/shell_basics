#!/usr/bin/python3
"""
This script converts binary to ascii.
"""
import sys

binary_list = sys.argv[1:]

ascii_string = ''.join([chr(int(bte, 2)) for bte in binary_list])
print(ascii_string)
