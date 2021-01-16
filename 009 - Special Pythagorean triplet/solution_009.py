#!/bin/python3
import math

import sys

triplets_max_mult = -1
triplets = set()


def clean_up():
    global triplets_max_mult
    global triplets
    triplets = set()
    triplets_max_mult = -1


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def possible_triples_v2(n):
    global triplets_max_mult

    for a in range(2, n // 3):

        b = ((2 * a * n) - (n ** 2)) // (2 * (a - n))
        c = n - (a + b)

        # print("a: {}, b: {}, c: {}, a+b+c={}".format(a, b, c, (a+b+c)))
        if is_pythagorean_triplet(a, b, c):
            triplets_max_mult = max(triplets_max_mult, (a * b * c))

    memory[n] = triplets_max_mult


memory = dict()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    if n % 2 == 1:
        # The circumference of a right triangle cannot be odd.
        print(-1)

    elif n in memory:
        # print("we've already calculated")
        print(memory[n])
    else:
        possible_triples_v2(n)
        # print("n =", n)
        print(triplets_max_mult)
        # print(triplets)

    # for item in (triplets):
    #     a,b,c = item
    #     print("{}\t=\t{}".format(item, (a*b*c)))

    # print('- - - - - - -')

    clean_up()
