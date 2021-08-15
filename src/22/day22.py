from src.problem import Problem


def part_a(data: list):
    p1_cards, p2_cards = data[0], data[1]

    while len(p1_cards) > 0 and len(p2_cards) > 0:
        play_move(p1_cards, p2_cards) if p1_cards[0] > p2_cards[0] else play_move(p2_cards, p1_cards)

    return sum(idx * card for idx, card in enumerate(reversed(p1_cards if len(p2_cards) == 0 else p2_cards), 1))


def play_move(winner_cards: list[int], loser_cards: list[int]) -> None:
    winner_cards.append(winner_cards.pop(0))
    winner_cards.append(loser_cards.pop(0))


def part_b(data: list):
    return None


def load(p: Problem):
    data = p.raw_data().split('\n\n')
    return [[int(d) for d in data[0].split('\n')[1:]], [int(d) for d in data[1].split('\n')[1:]]]


if __name__ == '__main__':
    problem = Problem(22)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
