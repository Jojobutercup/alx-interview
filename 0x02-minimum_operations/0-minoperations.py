#!/usr/bin/python3

""" A method that calculates the fewest
number of operations needed to result in exactly
n H characters in the file
"""


def minOperations(n):
    """ If n is less than or equal to 1,
    #it is impossible to obtain n Hs, so we return 0 """
    if n <= 1:
        return 0

    """ Initialize a variable ops to 0 to keep
    #track of the number of operations performed"""
    ops = 0

    """ We use a while loop to continuously check
    if n is divisible by any number i (2<=i<=n)"""
    i = 2
    while i <= n:
        """ If n is divisible by i, we copy all
        Hs and paste (i-1) times to obtain (i) Hs"""
        while n % i == 0:
            ops += i
            n //= i
        i += 1

    # Finally, we return the number of operations performed
    return ops
