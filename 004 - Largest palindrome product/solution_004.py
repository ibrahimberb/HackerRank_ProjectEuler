#!/bin/python3

import sys


def check_multiples(n):
    """
    Check if the given number n is a multiple of two 3-digit numbers.
    """
    palindrome_generator = generate_palindrome_numbers(n)
    largest_palindrome = next(palindrome_generator)
    # print("LARGEST PALINDROME:", largest_palindrome)
    for i in range(100, 1000):
        if largest_palindrome % i == 0 and len(str(largest_palindrome // i)) == 3:
            return largest_palindrome
    # get next palindrome
    largest_palindrome = next(palindrome_generator)
    return check_multiples(largest_palindrome)


def generate_palindrome_numbers(n):
    while True:
        n_string = str(n)
        if n_string == n_string[::-1]:
            break

        n = n - 1

    yield n
    yield from generate_palindrome_numbers(n - 1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(check_multiples(n - 1))
