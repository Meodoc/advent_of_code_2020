from src.problem import Problem


def transform(x: int, subj: int):
    return (x * subj) % 20201227


def part_a(pub_card: int, pub_door: int):
    x, loop = 1, 1
    while True:
        x = transform(x, subj=7)
        if x in (pub_card, pub_door):
            break
        loop += 1

    subject = pub_card if x == pub_door else pub_card
    x = 1
    for _ in range(loop):
        x = transform(x, subject)

    return x


def load(p: Problem):
    return p.data(dtype=int)


if __name__ == '__main__':
    problem = Problem(25, test=False)

    print(part_a(*load(problem)))

    # problem.submit(part_a(*load(problem)), 'a')
