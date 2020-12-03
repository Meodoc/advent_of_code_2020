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
    cols = [0, 0, 0, 0, 0]
    for r, line in enumerate(data):
        if line[cols[0]] == '#':
            n_trees[0] += 1
        cols[0] = (cols[0] + 1) % len(line)
        if line[cols[1]] == '#':
            n_trees[1] += 1
        cols[1] = (cols[1] + 3) % len(line)
        if line[cols[2]] == '#':
            n_trees[2] += 1
        cols[2] = (cols[2] + 5) % len(line)
        if line[cols[3]] == '#':
            n_trees[3] += 1
        cols[3] = (cols[3] + 7) % len(line)
        if r % 2 == 0:
            if line[cols[4]] == '#':
                n_trees[4] += 1
            cols[4] = (cols[4] + 1) % len(line)

    return n_trees[0] * n_trees[1] * n_trees[2] * n_trees[3] * n_trees[4]


if __name__ == '__main__':
    problem = Problem(3)
    data = problem.get_data()
    
    print(part_b())
    problem.submit(part_a(), 'a')
    problem.submit(part_b(), 'b')
