#!/usr/bin/python3


def validUTF8(data):
    # Variable to track the number of expected bytes for the next character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if it is a continuation byte (starts with 10)
        if num >> 6 == 0b10:
            # If there are no expected bytes, it is an invalid encoding
            if num_bytes == 0:
                return False
            # Decrement the number of expected bytes
            num_bytes -= 1
        else:
            # Check the number of bytes for the next character
            if num_bytes > 0:
                return False
            # Determine the number of expected bytes
            # based on the first few bits
            if num >> 7 == 0b0:
                num_bytes = 0  # 1 byte character
            elif num >> 5 == 0b110:
                num_bytes = 1  # 2 byte character
            elif num >> 4 == 0b1110:
                num_bytes = 2  # 3 byte character
            elif num >> 3 == 0b11110:
                num_bytes = 3  # 4 byte character
            else:
                return False  # Invalid starting byte

    # If there are remaining expected bytes, it is an invalid encoding
    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115,
            32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
