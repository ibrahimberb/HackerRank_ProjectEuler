#!/bin/python3

import sys
import math

# two dictionaries
# nth_prime_dict = {1:2, 2:3, 3:5}
largest_prime_used = 2

# Summation of all primes upto n. (n does not have to be a prime.)
# n = 10: {2, 3, 5} =
primes_sum_dict = {2: 2}


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_last_prime(n):
    while not is_prime(n):
        n = n - 1
    return n


def find_sum(n):
    # if we already calculated, then return the answer directly
    try:
        return primes_sum_dict[find_last_prime(n)]
    except KeyError:
        global largest_prime_used
        # print("we're gonna have to calculate it, starting from {}".format(largest_prime_used))
        for i in range(largest_prime_used + 1, n + 1):
            if is_prime(i) and i not in primes_sum_dict:
                primes_sum_dict[i] = primes_sum_dict[largest_prime_used] + i
                largest_prime_used = i


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # print(primes_sum_dict)
    find_sum(n)
    # print(primes_sum_dict)
    # print(largest_prime_used)
    print(primes_sum_dict[find_last_prime(n)])
    # print("- - - - - - - - - - - - -")
