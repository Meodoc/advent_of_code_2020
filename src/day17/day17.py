from src.problem import Problem

import numpy as np
from funcy import lmap
from scipy.signal import convolve

ACTIVE = 1
INACTIVE = 0

KERNEL = np.array([
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]],
    [[1, 1, 1],
     [1, 10, 1],
     [1, 1, 1]],
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]])


def part_a(data):
    for _ in range(6):
        data = convolve_cubes(data)
    return np.count_nonzero(data == 1)


def part_b():
    return None


def convolve_cubes(data: np.ndarray):
    c = convolve(data, KERNEL, mode='full')
    for i, x in enumerate(c):
        for j, y in enumerate(x):
            for k, _ in enumerate(y):
                if c[i][j][k] > 10:
                    c[i][j][k] = 1 if c[i][j][k] in [12, 13] else 0
                elif c[i][j][k] < 10:
                    c[i][j][k] = 1 if c[i][j][k] == 3 else 0
    return c


def load():
    dim = len(problem.data()[0])
    zeros = np.zeros((dim, dim), dtype=np.int64)
    init = np.array([lmap(lambda c: ACTIVE if c == '#' else INACTIVE, line) for line in problem.data()], dtype=np.int64)
    return np.stack((zeros, init, zeros))


if __name__ == '__main__':
    problem = Problem(17)
    data = load()

    problem.submit(part_a(data), 'a')
    # problem.submit(part_b(), 'b')
