#!/usr/bin/python3
"""
Task 0: UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid UTF-8 encoding.
    """
    bytes_to_process = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if bytes_to_process == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                bytes_to_process += 1
            if bytes_to_process == 0:
                continue
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        bytes_to_process -= 1
    return bytes_to_process == 0
