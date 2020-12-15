from src.problem import Problem

from copy import deepcopy


def part_a():
    return play(2020)


def part_b():
    return play(30_000_000)


def play(turns):
    memory = deepcopy(data)
    last_num = list(data.keys())[-1]
    for turn in range(len(data), turns):
        # Use double assignment to avoid temporarily saving the last_num for storing its turn
        memory[last_num], last_num = turn, 0 if last_num not in memory else turn - memory[last_num]
    return last_num


def load():
    return {int(num): turn for turn, num in enumerate(problem.data()[0].split(','), 1)}


if __name__ == '__main__':
    problem = Problem(15)
    data = load()

    problem.submit(part_a(), 'a')  # 1194
    problem.submit(part_b(), 'b')  # 48710
