from src.problem import Problem

import itertools as it


def part_a(data: list):
    diffs = list(map(lambda x1, x2: x2 - x1, data, data[1:]))
    return diffs.count(1) * diffs.count(3)


def part_b(data: list):
    print(data)
    arr = count_arr(data)

    return arr


def count_arr(data: list):
    arr = 1
    for i in range(len(data)):
        for skip in range(2, 4):
            if i + skip < len(data) and data[i + skip] - data[i] <= 3:
                arr += count_arr(data[i + skip:])
                # print(data[:i + 1] + data[i + skip:])
            else:
                break
    return arr


def load(p: Problem):
    return sorted(p.data(dtype=int) + [0, max(p.data(dtype=int)) + 3])  # Append charging outlet and adapter


if __name__ == '__main__':
    problem = Problem(10, test=True)

    # print(part_a(load(problem)))
    print(part_b(load(problem)))

    # test solution: 19208

    # 36132988816414656965872925540352 too high
    # 2251799813685248 too high

    # problem.submit(part_a(load(problem)), 'a')  # 2775
    # problem.submit(part_b(load(problem)), 'b')
