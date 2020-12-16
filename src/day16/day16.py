from src.problem import Problem

import re

RULE_PATTERN = re.compile(r'^([a-z|\s]+): (\d+)-(\d+) or (\d+)-(\d+)')


def _rule_closure(min1, max1, min2, max2):
    return lambda x: int(min1) <= int(x) <= int(max1) or int(min2) <= int(x) <= int(max2)


def part_a():
    rules = {(m := RULE_PATTERN.match(line)).group(1): _rule_closure(m.group(2), m.group(3), m.group(4), m.group(5))
             for line in data[0]}

    # Return the sum of all fields that match no rule
    return sum(int(field) for ticket in data[2] for field in ticket.split(',')
               if all(not rules[k](field) for k, _ in rules.items()))


def part_b():
    return None


def load():
    data = problem.data()
    your_ticket = data.index('your ticket:')
    nearby_tickets = data.index('nearby tickets:')
    return [data[:your_ticket - 1], data[your_ticket + 1], data[nearby_tickets + 1:]]


if __name__ == '__main__':
    problem = Problem(16)
    data = load()

    print(part_a())
    problem.submit(part_a(), 'a')  # 20091
    # problem.submit(part_b(), 'b')
