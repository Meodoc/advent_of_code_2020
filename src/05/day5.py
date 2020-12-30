from src.problem import Problem


def part_a():
    seat_ids = []
    for line in data:
        row, col = parse_boarding_pass(line)
        seat_ids.append(row * 8 + col)

    return max(seat_ids)


def part_b():
    seats = dict()
    for line in data:
        row, col = parse_boarding_pass(line)
        seat_id = row * 8 + col
        seats[seat_id] = (row, col)

    ordered_seats = dict(sorted(seats.items(), key=lambda item: item[0]))
    last_id = 0
    for id, pos in ordered_seats.items():
        if pos[0] == 0 or pos[0] == 127:  # ignore first and last row
            continue
        if id == last_id + 2:
            return id-1
        last_id = id


def parse_boarding_pass(actions):
    row_actions = actions[:7]
    col_actions = actions[7:]
    row_area = [0, 127]
    col_area = [0, 7]

    for row_action in row_actions:
        row_area = binary_partitioning(row_area, row_action)
    for col_action in col_actions:
        col_area = binary_partitioning(col_area, col_action)

    assert row_area[0] == row_area[1]
    assert col_area[0] == col_area[1]

    return row_area[0], col_area[0]


def binary_partitioning(area, action):
    lower = area[0]
    upper = area[1]
    middle = int((upper + lower) / 2)
    if action == 'F' or action == 'L':
        return [lower, middle]
    if action == 'B' or action == 'R':
        return [middle + 1, upper]


def load():
    return problem.data()


if __name__ == '__main__':
    problem = Problem(5)
    data = load()

    problem.submit(part_a(), 'a')  # 974
    problem.submit(part_b(), 'b')  # 646
