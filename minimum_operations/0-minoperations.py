#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n <= 1:
        return 0
    
    div = 2
    ope = 0

    while(n > 1):
        if (n % div == 0):
            n //= div
            ope += div
        else:
            div += 1

    return ope
