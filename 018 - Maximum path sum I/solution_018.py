"""
HackerRank Project Euler Problem 18: Maximum path sum I
"""

general_list = []


def add_up(above_list, below_list):
    if len(below_list) == 2:
        for i in range(len(below_list)):
            below_list[i] = below_list[i] + above_list[0]

    else:
        # Head
        below_list[0] = below_list[0] + above_list[0]

        # Tail
        below_list[-1] = below_list[-1] + above_list[-1]

        # Middle
        for i in range(1, len(below_list) - 1):
            below_list[i] = below_list[i] + max(above_list[i], above_list[i - 1])


for _ in range(int(input())):
    for _ in range(int(input())):
        general_list.append(list(map(int, input().split())))

    for inner_list_index in range(1, len(general_list)):
        add_up(general_list[inner_list_index - 1], general_list[inner_list_index])

    print(max(general_list[-1]))
    general_list = []
