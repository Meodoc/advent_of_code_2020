from src.problem import Problem

import re


# TODO: weird interaction when dict without indices
def part_a():
    yes_answers = dict()
    for i, group in enumerate(data):
        yes_answers[i] = set()
        for person in group.split('\n'):
            for yes_answer in person:
                yes_answers[i].add(yes_answer)
    result = 0
    for i, _ in enumerate(yes_answers):
        result += len(yes_answers[i])

    return result


def part_b():
    yes_answers = dict()
    for i, group in enumerate(data):
        yes_answers[i] = set()
        person_answers = dict()
        for j, person in enumerate(group.split('\n')):
            person_answers[j] = set()
            for yes_answer in person:
                person_answers[j].add(yes_answer)

        yes_answers[i] = set.intersection(*[x for x in person_answers.values()])

    result = 0
    for i, _ in enumerate(yes_answers):
        result += len(yes_answers[i])
    return result


def load():
    return problem.data(delim='\n\n')


if __name__ == '__main__':
    problem = Problem(6)
    data = load()

    # 6624 too low
    print(part_b())  # 6625
    #problem.submit(part_a(), 'a')
    problem.submit(part_b(), 'b')
