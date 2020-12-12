from src.problem import Problem


def part_a():
    diffs = list(map(lambda x1, x2: x2 - x1, data, data[1:]))
    return diffs.count(1) * diffs.count(3)


def part_b():
    return None


def load():
    return sorted((data := problem.data(dtype=int)) + [0, max(data) + 3])  # Append charging outlet and adapter


if __name__ == '__main__':
    problem = Problem(10)
    data = load()

    problem.submit(part_a(), 'a')  # 2775
    # problem.submit(part_b(), 'b')
