from src.problem import Problem


def part_a():
    n_trees = 0
    c = 0
    for line in data:
        if line[c] == '#':
            n_trees += 1
        c = (c + 3) % len(line)

    return n_trees


def part_b():
    n_trees = [0, 0, 0, 0, 0]
    c = [0, 0, 0, 0, 0]
    for r, line in enumerate(data):
        if line[c[0]] == '#':
            n_trees[0] += 1
        c[0] = (c[0] + 1) % len(line)
        if line[c[1]] == '#':
            n_trees[1] += 1
        c[1] = (c[1] + 3) % len(line)
        if line[c[2]] == '#':
            n_trees[2] += 1
        c[2] = (c[2] + 5) % len(line)
        if line[c[3]] == '#':
            n_trees[3] += 1
        c[3] = (c[3] + 7) % len(line)
        if r % 2 == 0:
            if line[c[4]] == '#':
                n_trees[4] += 1
            c[4] = (c[4] + 1) % len(line)

    return n_trees[0] * n_trees[1] * n_trees[2] * n_trees[3] * n_trees[4]


def load():
    data = problem.data()
    return data


if __name__ == '__main__':
    problem = Problem(3)
    data = load()

    problem.submit(part_a(), 'a')  # 292
    problem.submit(part_b(), 'b')  # 9354744432
