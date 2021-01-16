import sys
import math

primes = dict()
last_computed = 0
last_prime = 0


# def get_ith_prime(n):
#     global last_computed
#     try:
#         return primes[n]
#     except KeyError:
#         prime_obj = generate_primes(generate_num(2))
#         print("we will compute from {} to {}".format(last_computed, (n)))
#         for i in range(last_computed, n + 1):
#             primes[i] = next(prime_obj)
#         last_computed = n
#         return primes[n]


# def generate_num(n):
#     yield n
#     yield from generate_num(n + 1)


# def generate_primes(s):
#     n = next(s)
#     yield n
#     yield from generate_primes(i for i in s if i % n != 0)


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_naive(n):
    try:
        print(primes[n])
    except KeyError:
        global last_computed
        global last_prime
        counter = last_computed + 1
        auxiliary = last_prime
        # print("we need to do new computation.\nLast computed: {}\nLast prime: {}".format(last_computed, last_prime))
        # print("computing from {} to {}".format(counter, n))
        while counter <= n:
            auxiliary += 1
            while not is_prime(auxiliary):
                auxiliary += 1
                # print("aux: ", auxiliary)
            last_computed = n
            last_prime = auxiliary
            primes[counter] = auxiliary
            counter += 1

        print(auxiliary)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime_naive(n)
    # print(primes)
