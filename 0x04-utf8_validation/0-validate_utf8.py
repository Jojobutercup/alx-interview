#!/usr/bin/python3
"""
Validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0

    for num in data:
        # Check if the number is a valid byte
        # (8 least significant bits)
        binary = format(num, '08b')

        # If it's the start of a new character
        if num_bytes == 0:
            # Check if the current byte is a single byte character
            for bit in binary:
                if bit == '0':
                    break
                num_bytes += 1

            # Check invalid number of bytes in the character
            if num_bytes == 0:
                continue

            ''' There is no need to check continuation byte,
            if character is a single byte '''
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check if the current byte is a continuation byte
            if not (binary[0] == '1' and binary[1] == '0'):
                return False

            # Decreases the count of leftover bytes
            num_bytes -= 1

    # bytes present have been validated
    return num_bytes == 0
