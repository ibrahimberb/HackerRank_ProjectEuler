#!/bin/python3

import sys


def get_sum(num_param, s):
    """
    Sum of a series: number_of_items * (first_term + last_term) / 2
    """
    first_term = s
    num_param = num_param - 1

    # Subtract 1 until it is divisible by s, to find last term.
    while num_param % s != 0:
        num_param = num_param - 1
    last_term = num_param

    n_items = ((last_term - first_term) // s) + 1

    total_sum = n_items * (first_term + last_term) >> 1
    return total_sum


def sum_of_multiples(n):
    sum_of_multiple_3s = get_sum(n, 3)
    sum_of_multiple_5s = get_sum(n, 5)
    sum_of_multiple_15s = get_sum(n, 15)

    # print(sum_of_multiple_3s)
    # print(sum_of_multiple_5s)
    # print(sum_of_multiple_15s)

    return sum_of_multiple_3s + sum_of_multiple_5s - sum_of_multiple_15s


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_of_multiples(n))
