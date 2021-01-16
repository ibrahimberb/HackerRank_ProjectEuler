#!/bin/python3

import sys
import math

grid = []
max_multiplication = 0


# not needed
def check_above(x, y):
    global grid
    if y < 3 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x][y - 1] * grid[x][y - 2] * grid[x][y - 3]


def check_below(x, y):
    global grid
    if y > 16 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]


# not needed
def check_left(x, y):
    global grid
    if x < 3 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x - 1][y] * grid[x - 2][y] * grid[x - 3][y]


def check_right(x, y):
    global grid
    if x > 16 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x + 1][y] * grid[x + 2][y] * grid[x + 3][y]


def check_diagonal_to_left_bottom(x, y):
    global grid
    if x < 3 or y > 16 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x - 1][y + 1] * grid[x - 2][y + 2] * grid[x - 3][y + 3]


def check_diagonal_to_right_bottom(x, y):
    global grid
    if x > 16 or y > 16 or grid[x][y] == 0:
        return 0

    return grid[x][y] * grid[x + 1][y + 1] * grid[x + 2][y + 2] * grid[x + 3][y + 3]


def check(x, y):
    global max_multiplication
    for checker in (check_below, check_right, check_diagonal_to_left_bottom, check_diagonal_to_right_bottom):
        max_multiplication = max(max_multiplication, checker(x, y))


for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

## two for loops to go over elements.
for i in range(20):
    for j in range(20):
        check(i, j)

print(max_multiplication)
