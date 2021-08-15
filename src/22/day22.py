from src.problem import Problem

PLAYER_1, PLAYER_2 = 0, 1


def part_a(data: list):
    p1_cards, p2_cards = data[0], data[1]

    while len(p1_cards) > 0 and len(p2_cards) > 0:
        _play_move(p1_cards, p2_cards) if p1_cards[0] > p2_cards[0] else _play_move(p2_cards, p1_cards)

    return _calculate_score((p1_cards if len(p2_cards) == 0 else p2_cards))


def part_b(data: list):
    p1_cards, p2_cards = data[0], data[1]
    winner = _recursive_game(p1_cards, p2_cards)

    return _calculate_score(p1_cards if winner == PLAYER_1 else p2_cards)


def _recursive_game(p1_cards: list[int], p2_cards: list[int]) -> int:
    deck_history = []

    while len(p1_cards) > 0 and len(p2_cards) > 0:
        if (p1_cards, p2_cards) in deck_history:
            return PLAYER_1

        deck_history.append((p1_cards.copy(), p2_cards.copy()))

        if len(p1_cards) > p1_cards[0] and len(p2_cards) > p2_cards[0]:
            winner = _recursive_game(p1_cards.copy()[1:p1_cards[0]+1], p2_cards.copy()[1:p2_cards[0]+1])
            _play_move(p1_cards, p2_cards) if winner == PLAYER_1 else _play_move(p2_cards, p1_cards)
        else:
            _play_move(p1_cards, p2_cards) if p1_cards[0] > p2_cards[0] else _play_move(p2_cards, p1_cards)

    return PLAYER_1 if len(p2_cards) == 0 else PLAYER_2


def _play_move(winner_cards: list[int], loser_cards: list[int]) -> None:
    winner_cards.append(winner_cards.pop(0))
    winner_cards.append(loser_cards.pop(0))


def _calculate_score(cards: list[int]) -> int:
    return sum(idx * card for idx, card in enumerate(reversed(cards), 1))


def load(p: Problem):
    data = p.raw_data().split('\n\n')
    return [[int(d) for d in data[0].split('\n')[1:]], [int(d) for d in data[1].split('\n')[1:]]]


if __name__ == '__main__':
    problem = Problem(22)

    # print(part_a(load(problem)))
    print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
