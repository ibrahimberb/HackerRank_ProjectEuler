import sys

fib_dict = {0: 1, 1: 1}


def sum_even_fib(n):
    total_even = 0
    i = 1
    while total_even + fib_efficient(i) <= n:
        current_fib = fib_efficient(i)
        if current_fib % 2 == 0:
            total_even += current_fib

        i += 1

    return total_even


def fib_efficient(n):
    try:
        return fib_dict[n]
    except KeyError:
        fib_new_val = fib_efficient(n - 1) + fib_efficient(n - 2)
        fib_dict[n] = fib_new_val
        return fib_new_val


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib_list = [1, 2]
    even_total = 2
    while fib_list[-1] + fib_list[-2] < n:
        fib_new = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_new)
        if fib_new % 2 == 0:
            even_total += fib_new
    # print(fib_list)
    print(even_total)
