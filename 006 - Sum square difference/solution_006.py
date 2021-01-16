#!/bin/python3

import sys


def square_of_sum(n):
    sum_of_elements = n * (n + 1) // 2
    return sum_of_elements ** 2


def sum_of_squares(n):
    result = (n) * (n + 1) * (2 * n + 1) // 6
    return result


def sum_square_difference(n):
    return square_of_sum(n) - sum_of_squares(n)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_square_difference(n))
