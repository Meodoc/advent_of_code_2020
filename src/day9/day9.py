from src.problem import Problem

import itertools as it


def part_a():
    for i, num in enumerate(data[26:]):
        preamble = data[i:26 + i]
        if num not in [sum(pair) for pair in it.combinations(preamble, 2)]:
            return num


def part_b():
    for start, _ in enumerate(data):
        for end, acc in enumerate(it.accumulate(data[start:]), start):
            if acc == invalid_num:
                return min(data[start:end]) + max(data[start:end])
            if acc > invalid_num:
                break


def load():
    return problem.data(dtype=int)


if __name__ == '__main__':
    problem = Problem(9)
    data = load()

    invalid_num = part_a()

    print(part_a())
    print(part_b())

    problem.submit(invalid_num, 'a')  # 85848519
    problem.submit(part_b(), 'b')  # 13414198
