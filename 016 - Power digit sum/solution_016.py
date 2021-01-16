"""
Euler Project #16: Power Digit Sum
"""


def sum_digits(exponential):
    number = 2 ** exponential
    number_string = str(number)
    total = 0
    for digit_string in number_string:
        digit = int(digit_string)
        total += digit

    return total


input_n = 10 ** 4

for _ in range(int(input())):
    print(sum_digits(int(input())))