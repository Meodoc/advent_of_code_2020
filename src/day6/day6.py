from src.problem import Problem

import re


# TODO: weird interaction when dict without indices
def part_a():
    return sum([len(answer) for answer in [set([answer for person in group.split('\n')for answer in person]) for group in data]])


def part_b():
    yes_answers = dict()
    for i, group in enumerate(data):
        yes_answers[i] = set()
        person_answers = dict()
        for j, person in enumerate(group.split('\n')):
            person_answers[j] = set()
            for yes_answer in person:
                person_answers[j].add(yes_answer)

        yes_answers[i] = set.intersection(*person_answers.values())

    result = 0
    for i, _ in enumerate(yes_answers):
        result += len(yes_answers[i])


    return result


def load():
    return problem.data(delim='\n\n')


if __name__ == '__main__':
    problem = Problem(6)
    data = load()


    print(part_a())
    # 6624 too low
    print(part_b())  # 6625
    #problem.submit(part_a(), 'a')
    #problem.submit(part_b(), 'b')


