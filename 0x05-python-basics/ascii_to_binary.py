#!/usr/bin/python3
"""
ascii text transform to binary
"""
import sys
ascii_string = sys.argv[1]

byte_list = bytearray(ascii_string,'utf8')

binary_list = [bin(byte) for byte in byte_list]

print(binary_list)
