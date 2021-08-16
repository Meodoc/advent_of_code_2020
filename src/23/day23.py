from src.problem import Problem
from collections import deque
from funcy import lmap
from itertools import cycle
import numpy as np


def play(follow: dict, total_cups: int, moves: int):
    current = list(follow.keys())[0]

    for _ in range(moves):
        # "pick up" cups
        pick_up = [_get_next(current, follow, i) for i in range(1, 4)]
        follow[current] = _get_next(current, follow, 4)

        # get destination cup
        destination = (current - 2) % total_cups + 1
        while destination in pick_up:
            destination = (destination - 2) % total_cups + 1

        # place cups clockwise to destination cup
        follow[pick_up[-1]] = follow[destination]
        follow[destination] = pick_up[0]

        # select new current cup
        current = follow[current]


def _get_next(cur: int, follow: dict, n: int) -> int:
    for _ in range(n):
        cur = follow[cur]
    return cur


def part_a(cups: list, follow: dict):
    play(follow, total_cups=len(cups), moves=100)

    result, current = '', 1
    for _ in range(len(cups) - 1):
        result += str(follow[current])
        current = follow[current]

    return result


def part_b(cups: list, follow: dict):
    total_cups = 1_000_000

    follow[cups[-1]] = len(cups) + 1
    for i in range(len(cups) + 1, total_cups):
        follow[i] = i % total_cups + 1
    follow[total_cups] = cups[0]

    play(follow, total_cups=total_cups, moves=10_000_000)

    return _get_next(1, follow, 1) * _get_next(1, follow, 2)


def load(p: Problem):
    data = lmap(int, p.raw_data())
    return [data, dict(zip(data, np.roll(data, -1)))]


if __name__ == '__main__':
    problem = Problem(23)

    # print(part_a(*load(problem)))
    # print(part_b(*load(problem)))

    # problem.submit(part_a(*load(problem)), 'a')
    problem.submit(part_b(*load(problem)), 'b')
