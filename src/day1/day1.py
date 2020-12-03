from src.problem import Problem
import itertools


def part_a():
    comb = itertools.combinations(data, 2)
    comb = [(a, b) for a, b in comb if a + b == 2020]
    return comb[0][0] * comb[0][1]


def part_b():
    comb = itertools.combinations(data, 3)
    comb = [(a, b, c) for a, b, c in comb if a + b + c == 2020]
    return comb[0][0] * comb[0][1] * comb[0][2]


if __name__ == '__main__':
    problem = Problem(1)
    data = problem.get_data(dtype=int)

    problem.submit(part_a(), 'a')
    problem.submit(part_b(), 'b')
