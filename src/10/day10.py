from src.problem import Problem


def part_a(data: list):
    diffs = list(map(lambda x1, x2: x2 - x1, data, data[1:]))
    return diffs.count(1) * diffs.count(3)


def part_b(data: list):
    arr = [0] * len(data)
    for i in reversed(range(0, len(data) - 3)):
        arr[i] = arr[i + 1]
        for skip in (2, 3):  # can possible only skip next or the next next item
            if data[i + skip] - data[i] <= 3:
                arr[i] += arr[i + skip] + 1

    return arr[0] + 1  # add the initial arrangement


def load(p: Problem):
    return sorted(p.data(dtype=int) + [0, max(p.data(dtype=int)) + 3])  # Append charging outlet and adapter


if __name__ == '__main__':
    problem = Problem(10, test=False)

    # print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
