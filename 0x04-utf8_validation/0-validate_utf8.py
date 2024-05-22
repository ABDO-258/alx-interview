#!/usr/bin/python3
"""scribt to check if data is a valid UTF-8"""


def validUTF8(data):
    """function to validate the data as utf-8"""
    # byte_representation = bytearray(xdata)
    # print(byte_representation)
    expected_continuation_bytes = 0
    bin_data = []
    for byte in data:
        if expected_continuation_bytes == 0:
            binary_representation = bin(byte)  # [2:]
            if byte >> 5 == 0b110:
                expected_continuation_bytes = 1
            elif byte >> 4 == 0b1110:
                expected_continuation_bytes = 2
            elif byte >> 3 == 0b11110:
                expected_continuation_bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            # Check continuation byte
            if byte >> 6 != 0b10:
                return False
            expected_continuation_bytes -= 1
        bin_data.append(binary_representation)
    # print(bin_data)
    return True
