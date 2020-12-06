from src.problem import Problem


def part_a():
    return sum([len(answer) for answer in [set([answer for person in group.split('\n') for answer in person]) for group in data]])


def part_b():
    return sum([len(answer) for answer in [set.intersection(*[set(answer for answer in person) for person in group.split('\n')]) for group in data]])


def load():
    return problem.data(delim='\n\n')


if __name__ == '__main__':
    problem = Problem(6)
    data = load()


    print(part_a())
    print(part_b())
    #problem.submit(part_a(), 'a')  # 6625
    #problem.submit(part_b(), 'b')


