# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from timeit import default_timer as timer

dictionary = dict()


def number_of_divisors(triangle):
    try:
        return dictionary[triangle]
    except KeyError:
        triangle_original = triangle
        number_of_divisor = 1
        count = 0
        while triangle % 2 == 0:
            triangle //= 2
            count += 1

        number_of_divisor *= (count + 1)

        current_divisor = 3
        while current_divisor <= math.sqrt(triangle):
            count = 0
            while triangle % current_divisor == 0:
                triangle //= current_divisor
                count += 1

            number_of_divisor *= (count + 1)
            current_divisor += 1

        if triangle > 1:
            number_of_divisor *= 2

        dictionary[triangle_original] = number_of_divisor
        return number_of_divisor


def triangular(num_param):
    return num_param * (num_param + 1) // 2


# def performance_measure(n, func):
#     start_time = timer()
#     number = 1
#     n_divisor = 1
#     while n > n_divisor:
#         number += 1
#         triangle = triangular(number)
#         n_divisor = func(triangle)

#     print(triangular(number))
#     end_time = timer()
#     print("Execution time: {}".format(round(end_time - start_time, 5)))


# performance_measure(1000, number_of_divisors)
# performance_measure(999, number_of_divisors)
# performance_measure(950, number_of_divisors)


for _ in range(int(input())):

    n_input = int(input())
    number = 1
    n_divisor = 1
    while n_input >= n_divisor:
        number += 1
        triangle = triangular(number)
        n_divisor = number_of_divisors(triangle)

    print(triangular(number))


