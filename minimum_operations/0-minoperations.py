#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    div, nb_operations = 2, 0

    if n <= 1:
        return 0
    while(n > 1):
        if (n % div == 0):
            n //= div
            nb_operations += div
        else:
            div += 1

    return nb_operations