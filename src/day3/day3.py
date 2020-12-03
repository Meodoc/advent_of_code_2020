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
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    for r, line in enumerate(data):
        if line[c0] == '#':
            n_trees[0] += 1
        c0 = (c0 + 1) % len(line)
        if line[c1] == '#':
            n_trees[1] += 1
        c1 = (c1 + 3) % len(line)
        if line[c2] == '#':
            n_trees[2] += 1
        c2 = (c2 + 5) % len(line)
        if line[c3] == '#':
            n_trees[3] += 1
        c3 = (c3 + 7) % len(line)
        if r % 2 == 0:
            if line[c4] == '#':
                n_trees[4] += 1
            c4 = (c4 + 1) % len(line)

    return n_trees[0] * n_trees[1] * n_trees[2] * n_trees[3] * n_trees[4]


if __name__ == '__main__':
    problem = Problem(3)
    data = problem.get_data()

    problem.submit(part_a(), 'a')
    problem.submit(part_b(), 'b')
