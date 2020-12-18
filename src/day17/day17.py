from src.problem import Problem

import numpy as np
from funcy import lmap
from scipy.signal import convolve

ACTIVE = 1
INACTIVE = 0

KERNEL_3D = np.array([
    np.ones((3, 3)),
    [[1, 1, 1],
     [1, 100, 1],
     [1, 1, 1]],
    np.ones((3, 3))
], dtype=np.int64)

KERNEL_4D = np.array([
    [np.ones((3, 3)), np.ones((3, 3)), np.ones((3, 3))],
    KERNEL_3D,
    [np.ones((3, 3)), np.ones((3, 3)), np.ones((3, 3))]
], dtype=np.int64)


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
    c = np.vectorize(map_cube_states)(c)
    return c


def map_cube_states(c):
    return 1 if c in [102, 103] or c == 3 else 0


def load():
    return np.array([lmap(lambda c: ACTIVE if c == '#' else INACTIVE, line) for line in problem.data()])


if __name__ == '__main__':
    problem = Problem(17)
    data = load()

    problem.submit(part_a(), 'a')  # 295
    problem.submit(part_b(), 'b')  # 1972
