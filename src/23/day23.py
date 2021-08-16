from src.problem import Problem
from collections import deque
from funcy import lmap
from itertools import cycle
import numpy as np


def part_a(data: list):
    cur_idx = 0
    current = data[cur_idx]
    total_cups = len(data)

    for _ in range(100):
        # pick up and remove
        pick_up = [data[idx % total_cups] for idx in range(cur_idx + 1, cur_idx + 4)]
        for i in range(3):
            data.remove(pick_up[i])

        # select destination cup
        destination = (current - 2) % total_cups + 1
        while destination not in data:
            destination = (destination - 2) % total_cups + 1
        dst_idx = data.index(destination)

        # insert picked up cups
        data[dst_idx + 1:dst_idx + 1] = pick_up

        # select new current cup
        cur_idx = (data.index(current) + 1) % total_cups
        current = data[cur_idx]

    data = deque(data)
    data.rotate(total_cups - data.index(1))
    return ''.join(lmap(str, list(data)[1:]))


def part_b(data: list):
    return None


def load(p: Problem):
    return lmap(int, p.raw_data())


if __name__ == '__main__':
    problem = Problem(23)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
