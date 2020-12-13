from src.problem import Problem

from math import ceil


def part_a():
    min_t = data[0]
    min_id = min(bus_t := {id: ceil(min_t/id) * id for id in data[1:]}, key=bus_t.get)
    return min_id * (bus_t[min_id] - min_t)


def part_b():
    return None


def load():
    return [int(problem.data()[0])] + [int(b) for b in filter(lambda b: b != 'x', problem.data()[1].split(','))]


if __name__ == '__main__':
    problem = Problem(13)
    data = load()

    problem.submit(part_a(), 'a')
    # problem.submit(part_b(), 'b')
