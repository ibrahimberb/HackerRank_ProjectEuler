#!/bin/python3

import sys


def get_product(num_string):
    product = 1
    for num in num_string:
        product *= int(num)
    return product


def largest_product(num, k):
    num_string = str(num)
    product = 0
    for i in range(len(num_string) - k + 1):
        product = max(product, get_product(num_string[i:i + k]))

    return product


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    # print(f"n={n}, k={k}, num={num}")
    print(largest_product(num, k))
