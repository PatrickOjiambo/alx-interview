#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """
Main file for testing
"""

    operations = 0
    i = 2
    while n > 1:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations
