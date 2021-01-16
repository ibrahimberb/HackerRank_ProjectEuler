"""
HackerRank Project Euler #15: Lattice paths
"""

from math import factorial as fact


def route_count(n, m):
    return (fact(n + m) // (fact(n) * fact(m))) % (10 ** 9 + 7)


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(route_count(n, m))
