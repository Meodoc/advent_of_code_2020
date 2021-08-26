from src.problem import Problem


def transform(x: int, subj: int):
    return (x * subj) % 20201227


def part_a(pub_card: int, pub_door: int):
    loop_card, loop_door = None, None
    x, loop = 1, 1
    while not loop_card or not loop_door:
        x = transform(x, subj=7)
        if x == pub_card:
            loop_card = loop
        if x == pub_door:
            loop_door = loop
        loop += 1

    x = 1
    for _ in range(loop_card):
        x = transform(x, subj=pub_door)

    return x


def load(p: Problem):
    return p.data(dtype=int)


if __name__ == '__main__':
    problem = Problem(25, test=False)

    # print(part_a(*load(problem)))

    # problem.submit(part_a(*load(problem)), 'a')
