from src.problem import Problem
from collections import deque
from funcy import lmap
import numpy as np


def part_a(data: list[int]):
    largest = len(data)
    cur_idx = 0
    for _ in range(10):
        cur_idx = _move(cur_idx % len(data), largest, data)
    print(data)
    return None


def _move(cur_idx: int, largest: int, data: list[int]) -> int:
    current = data[cur_idx]
    pick_up = data[cur_idx + 1:(cur_idx + 4) % len(data)]
    for cup in pick_up:
        data.remove(cup)
    # pick_up = [data.pop((cur_idx + 1) % len(data)) for _ in range(3)]
    dst_cup = _find_dst_cup(current, largest, pick_up, data)
    data[dst_cup + 1:dst_cup + 1] = pick_up
    return data.index(current) + 1


def _find_dst_cup(current: int, largest: int, pick_up: list[int], data: list[int]) -> int:
    current = wrap(current - 1, 1, largest)
    while current in pick_up:
        current = wrap(current - 1, 1, largest)
    return data.index(current)


def wrap(n: int, smallest: int, largest: int) -> int:
    return (n - smallest) % largest + smallest


def part_b(data: list):
    return None


def load(p: Problem):
    return lmap(int, p.raw_test_data())


if __name__ == '__main__':
    problem = Problem(23)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
