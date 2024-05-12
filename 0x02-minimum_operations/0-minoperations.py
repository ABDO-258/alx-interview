#!/usr/bin/python3
""" mini operation interview """


def minOperations(n):
    """ get the minimum operation to get to n H"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n /= divisor
        else:
            divisor += 1
    return operations
