from src.problem import Problem

import copy
import itertools as it

FREE = "L"
OCCUPIED = "#"
FLOOR = "."

POLICY_A = {FREE: lambda r, c, seats: OCCUPIED if _n_adj_occupied(r, c, seats) == 0 else FREE,
            OCCUPIED: lambda r, c, seats: FREE if _n_adj_occupied(r, c, seats) >= 4 else OCCUPIED,
            FLOOR: lambda r, c, seats: FLOOR}

POLICY_B = {FREE: lambda r, c, seats: OCCUPIED if _n_visible_occupied(r, c, seats) == 0 else FREE,
            OCCUPIED: lambda r, c, seats: FREE if _n_visible_occupied(r, c, seats) >= 5 else OCCUPIED,
            FLOOR: lambda r, c, seats: FLOOR}


def _free_occ_iter(seats):
    return it.filterfalse(lambda t: seats[t[0]][t[1]] == FLOOR, it.product(range(len(data)), range(len(data[0]))))


def part_a():
    return n_occupied_in_equilibrium(data, 'a')


def part_b():
    return n_occupied_in_equilibrium(data, 'b')


def n_occupied_in_equilibrium(data, policy):
    state = copy.deepcopy(data)
    prev_state = None
    while True:
        state = apply_policy(state, policy)
        if prev_state and \
                all(prev_state[r][c] == state[r][c] for r, c in _free_occ_iter(state)):
            break
        prev_state = state
    return sum(r.count(OCCUPIED) for r in state)


def apply_policy(seats, policy):
    new_seats = copy.deepcopy(seats)
    for r, c in _free_occ_iter(seats):
        new_seats[r][c] = POLICY_A[seats[r][c]](r, c, seats) if policy == 'a' else POLICY_B[seats[r][c]](r, c, seats)
    return new_seats


def load():
    return [[col for col in row] for row in problem.data()]


if __name__ == '__main__':
    problem = Problem(11)
    data = load()

    problem.submit(part_a(), 'a')  # 2243
    problem.submit(part_b(), 'b')  # 2027


def _n_adj_occupied(r0, c0, seats):
    n = 0
    for r, c in it.filterfalse(lambda t: t == (r0, c0), it.product(range(r0 - 1, r0 + 2), range(c0 - 1, c0 + 2))):
        if 0 <= r < len(seats) and 0 <= c < len(seats[0]) and seats[r][c] == OCCUPIED:
            n += 1
    return n


# Sorry for that ugly solution
def _n_visible_occupied(r0, c0, seats):
    n = 0
    # Down
    for r in range(r0 + 1, len(seats)):
        if seats[r][c0] == OCCUPIED:
            n += 1
            break
        if seats[r][c0] == FREE:
            break
    # Up
    for r in reversed(range(0, r0)):
        if seats[r][c0] == OCCUPIED:
            n += 1
            break
        if seats[r][c0] == FREE:
            break
    # Right
    for c in range(c0 + 1, len(seats[0])):
        if seats[r0][c] == OCCUPIED:
            n += 1
            break
        if seats[r0][c] == FREE:
            break
    # Left
    for c in reversed(range(0, c0)):
        if seats[r0][c] == OCCUPIED:
            n += 1
            break
        if seats[r0][c] == FREE:
            break
    # Diagonal down-right
    for r, c in zip(range(r0 + 1, len(seats)), range(c0 + 1, len(seats[0]))):
        if seats[r][c] == OCCUPIED:
            n += 1
            break
        if seats[r][c] == FREE:
            break
    # Diagonal up-left
    for r, c in zip(reversed(range(0, r0)), reversed(range(0, c0))):
        if seats[r][c] == OCCUPIED:
            n += 1
            break
        if seats[r][c] == FREE:
            break
    # Diagonal down-left
    for r, c in zip(range(r0 + 1, len(seats)), reversed(range(0, c0))):
        if seats[r][c] == OCCUPIED:
            n += 1
            break
        if seats[r][c] == FREE:
            break
    # Diagonal up-right
    for r, c in zip(reversed(range(0, r0)), range(c0 + 1, len(seats[0]))):
        if seats[r][c] == OCCUPIED:
            n += 1
            break
        if seats[r][c] == FREE:
            break
    return n
