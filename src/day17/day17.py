from src.problem import Problem

import numpy as np
from scipy.signal import convolve

KERNEL_3D = np.ones((3, 3, 3), dtype=np.int64)
KERNEL_3D[1][1][1] = 100

KERNEL_4D = np.ones((3, 3, 3, 3), dtype=np.int64)
KERNEL_4D[1][1][1][1] = 100


def part_a():
    pocket_dim = np.expand_dims(data, axis=0)
    for _ in range(6):
        pocket_dim = convolve_cubes(pocket_dim, KERNEL_3D)
    return np.count_nonzero(pocket_dim == 1)


def part_b():
    pocket_dim = np.expand_dims(np.expand_dims(data, axis=0), axis=0)
    for _ in range(6):
        pocket_dim = convolve_cubes(pocket_dim, KERNEL_4D)
    return np.count_nonzero(pocket_dim == 1)


def convolve_cubes(grid: np.ndarray, kernel: np.ndarray):
    c = convolve(grid, kernel, mode='full')
    c = np.vectorize(lambda elem: elem in [3, 102, 103])(c)
    return c


def load():
    return np.array([list(line) for line in problem.data()]) == '#'


if __name__ == '__main__':
    problem = Problem(17)
    data = load()

    problem.submit(part_a(), 'a')  # 295
    problem.submit(part_b(), 'b')  # 1972
