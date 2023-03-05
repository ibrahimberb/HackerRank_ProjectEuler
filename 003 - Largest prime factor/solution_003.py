#!/bin/python3

import sys
import math

highest_prime_factor = 0


def clear_globals():
    global highest_prime_factor

    highest_prime_factor = 0


def find_largest_prime_factor(n):
    global highest_prime_factor

    prime, divisor = is_prime(n)
    highest_prime_factor = divisor
    if prime:
        return divisor
    else:
        find_largest_prime_factor(n // divisor)


def is_prime(num):
    if num < 2:
        return False, num
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False, i

    return True, num


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    find_largest_prime_factor(n)
    print(highest_prime_factor)
    clear_globals()
