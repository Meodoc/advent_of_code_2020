from src.problem import Problem

from collections import deque, defaultdict
from functools import partial
from copy import deepcopy


def part_a():
    return play(2020)


def part_b():
    return play(30_000_000)


def play(turns):
    memory = deepcopy(data)
    last_num = list(data.keys())[-1]
    turn = len(data) + 1
    while turn <= turns:
        if len(memory[last_num]) == 1:
            last_num = 0
        else:
            last_num = memory[last_num][1] - memory[last_num][0]
        memory[last_num].append(turn)
        turn += 1
    return last_num


def load():
    return defaultdict(partial(deque, maxlen=2), {int(num): deque([turn], maxlen=2)
                                                  for turn, num in enumerate(problem.data()[0].split(','), 1)})


if __name__ == '__main__':
    problem = Problem(15)
    data = load()

    problem.submit(part_a(), 'a')  # 1194
    problem.submit(part_b(), 'b')  # 48710
