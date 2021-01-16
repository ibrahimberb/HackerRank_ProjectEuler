#!/bin/python3

import sys
import math

highest_prime_factor = 0


def clear_globals():
    global highest_prime_factor

    highest_prime_factor = 0


def find_largest_prime_factor_v2(n):
    global highest_prime_factor

    prime, divisor = is_prime(n)
    highest_prime_factor = divisor
    if prime:
        return divisor
    else:
        find_largest_prime_factor_v2(n // divisor)


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False, i

    return True, n


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    find_largest_prime_factor_v2(n)
    print(highest_prime_factor)
    clear_globals()
