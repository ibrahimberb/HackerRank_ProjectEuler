limit = 5_000_001
results = [False] * limit
results[1] = 0

records = []

last_max = -1


def next_collatz(num):
    """Return next collatz term"""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


def create_collatz_seq(num):
    if num == 1:
        return 0

    if num < limit and results[num] != False:
        return results[num]

    else:
        result = 1 + create_collatz_seq(next_collatz(num))
        if num < limit:
            results[num] = result

        return result


for i in range(1, limit):
    create_collatz_seq(i)

record_ind = -1
for index, result in enumerate(results):
    if result >= last_max:
        last_max = result
        record_ind = (index + 1)

    records.append(record_ind)

for _ in range(int(input())):
    n_input = int(input())
    print(records[n_input] - 1)
