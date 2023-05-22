#!/usr/bin/python3
"""
Validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0

    for num in data:
        # Check if the number is a valid byte
        # (8 least significant bits)
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            # Check if the current byte is a single byte character
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7) != 0:
                return False
        else:
            # Check if the current byte is a continuation byte
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
