#!/usr/bin/python3
"""comments here"""


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
