from src.problem import Problem

from math import floor, ceil


def part_a():
    min_t = int_data[0]
    min_id = min(bus_t := {id: ceil(min_t/id) * id for id in int_data[1:]}, key=bus_t.get)
    return min_id * (bus_t[min_id] - min_t)


def part_b():
    data_b = data[1:]
    int_data_b = int_data[1:]
    max_id = max(int_data_b)
    max_id_idx = next(idx for idx, id in enumerate(data_b) if id != 'x' and int(id) == max_id)
    first_id = int_data_b[0]
    bus_offset = {int(id): idx - max_id_idx for idx, id in enumerate(data_b) if id != 'x' and int(id) != max_id}

    timestamp = -1
    i = 1
    while True:
        t0 = i * max_id
        matching = 0
        for id, offset in bus_offset.items():
            nearest = nearest_timestamp(id, t0, offset)
            if id == first_id:
                timestamp = nearest
            if nearest - t0 == offset:
                matching += 1
            else:
                break
        if matching == len(int_data_b) - 1:
            break
        i += 1
        if i % 1_000_000 == 0:
            print(timestamp)

    return timestamp


def nearest_timestamp(id: int, t0: int, offset: int):
    if offset < 0:
        return floor(t0/id) * id
    elif offset > 0:
        return ceil(t0/id) * id


def load():
    return [int(problem.data()[0])] + [b for b in problem.data()[1].split(',')]


if __name__ == '__main__':
    problem = Problem(13)
    data = load()
    int_data = [int(d) for d in filter(lambda b: b != 'x', data)]

    answer_b = part_b()
    print(answer_b)
    # problem.submit(part_a(), 'a')
    problem.submit(answer_b, 'b')
