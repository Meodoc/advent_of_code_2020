from src.problem import Problem

from math import floor, ceil, gcd, prod
from itertools import combinations


def part_a():
    min_t = bus_data[0]
    min_id = min(bus_t := {id: ceil(min_t/id) * id for id in bus_data[1:]}, key=bus_t.get)
    return min_id * (bus_t[min_id] - min_t)


def part_b():
    # Calculate the minimal timestamp using the chinese remainder theorem
    # https://www.youtube.com/watch?v=zIFehsBHB8o

    # Ensure that the gcd of all the bus id's is 1 for the theorem to apply
    assert max(gcd(c[0], c[1]) for c in combinations(bus_data[1:], 2)) == 1

    # Calculate factor lists
    ids = [id for id in (bus_data[1:])]
    b = [int(id) - offset for offset, id in (enumerate(data[1:])) if id != 'x']
    N = [prod([id for i, id in enumerate(ids) if i != j]) for j in range(len(ids))]
    x = [pow(N[i], -1, ids[i]) for i in range(len(ids))]

    # Calculate result
    x = sum(b[i] * N[i] * x[i] for i in range(len(ids)))

    # Minimal result is the smallest x in the mod (id1 * id2, ..., * idn) space that is > 0
    return find_min_result(x, prod([id for id in ids]))


def find_min_result(x, y):
    return x - floor(x/y) * y


def load():
    return [int(problem.data()[0])] + [b for b in problem.data()[1].split(',')]


if __name__ == '__main__':
    problem = Problem(13)
    data = load()
    bus_data = [int(d) for d in filter(lambda b: b != 'x', data)]

    problem.submit(part_a(), 'a')  # 8063
    problem.submit(part_b(), 'b')  # 775230782877242
