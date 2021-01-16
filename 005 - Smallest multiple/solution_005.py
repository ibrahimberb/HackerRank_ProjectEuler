#!/bin/python3

import sys

temp_dict = dict()
factors_count = dict()


def clean_temp():
    global temp_dict
    temp_dict = dict()


def clean_factors_count():
    global factors_count
    factors_count = dict()


def clean_up():
    clean_temp()
    clean_factors_count()


def multiply(d):
    result = 1
    # print(d)
    for key, value in d.items():
        result *= key ** value
    print(result)


def find_smallest_multiple(n):
    for i in range(2, n + 1):
        find_prime_factors(i)
        for key, value in temp_dict.items():
            if key not in factors_count:
                factors_count[key] = value
            else:
                factors_count[key] = max(factors_count[key], value)
        clean_temp()
    multiply(factors_count)


def find_prime_factors(n):
    prime_generator_obj = sieve(generate_num(2))
    prime = next(prime_generator_obj)
    while n >= prime:
        while n % prime == 0:
            if prime not in temp_dict:
                temp_dict[prime] = 1
            else:
                temp_dict[prime] += 1
            n = n // prime
        # get next prime
        prime = next(prime_generator_obj)
    # print(temp_dict)


def generate_num(n):
    yield n
    yield from generate_num(n + 1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    find_smallest_multiple(n)
    clean_up()
