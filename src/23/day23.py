from src.problem import Problem
from funcy import lmap
from math import prod
import numpy as np


def play(nxt: dict, moves: int):
    highest, cur = len(nxt), list(nxt.keys())[0]

    for _ in range(moves):
        # pick up and unlink cups
        pick_up = (nxt_4 := list(traverse(nxt, start=cur, steps=4)))[0:3]
        nxt[cur] = nxt_4[-1]

        # find destination cup
        dest = (cur - 2) % highest + 1
        while dest in pick_up:
            dest = (dest - 2) % highest + 1

        # link cups clockwise to destination cup
        nxt[dest], nxt[pick_up[-1]] = pick_up[0], nxt[dest]

        # assign next current cup
        cur = nxt[cur]


def traverse(nxt: dict, start: int, steps: int) -> iter:
    for _ in range(steps):
        start = nxt[start]
        yield start


def part_a(nxt: dict):
    play(nxt, moves=100)
    return ''.join(lmap(str, traverse(nxt, start=1, steps=len(nxt) - 1)))


def part_b(nxt: dict):
    total_cups = 1_000_000
    first, last = list(nxt.keys())[0], list(nxt.keys())[-1]

    # link new cups
    nxt[last], nxt[total_cups] = len(nxt) + 1, first
    for i in range(len(nxt), total_cups):
        nxt[i] = i + 1

    play(nxt, moves=10_000_000)
    return prod(traverse(nxt, start=1, steps=2))


def load(p: Problem):
    data = lmap(int, p.raw_data())
    return dict(zip(data, np.roll(data, -1)))


if __name__ == '__main__':
    problem = Problem(23)

    # print(part_a(load(problem)))  # 26354798
    # print(part_b(load(problem)))  # 166298218695

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
