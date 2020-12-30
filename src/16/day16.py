from src.problem import Problem

from math import prod
import re

RULE_PATTERN = re.compile(r'^([a-z|\s]+): (\d+)-(\d+) or (\d+)-(\d+)')


def _rule_closure(min1, max1, min2, max2):
    return lambda x: int(min1) <= int(x) <= int(max1) or int(min2) <= int(x) <= int(max2)


def part_a():
    # Return the sum of all fields that match no rule
    return sum(int(field) for ticket in data[2] for field in ticket.split(',')
               if all(not rules[k](field) for k, _ in rules.items()))


def part_b():
    # Filters for the tickets where every field fulfills at least one rule
    valid_tickets = [ticket for ticket in data[2]
                     if all(any(rules[r](field) for r, _ in rules.items()) for field in ticket.split(','))]

    # Searches for unique rules until there is a rule entry for every data position in the 'rule_positions' dict
    rule_positions = dict()
    while len(rule_positions) < (len(data[1].split(','))):
        rule, pos = find_unique_rule(rules, valid_tickets)
        rule_positions[rule] = pos
        rules.pop(rule)

    # Returns the product of all fields in own ticket that start with 'departure'
    return prod(int(field) for pos, field in enumerate(data[1].split(',')) if pos in
                [r_pos for rule, r_pos in rule_positions.items() if rule.startswith('departure')])


#  Searches for every position 'pos' a rule that uniquely applies to the position, meaning no other rule is allowed to
#  apply to this position.
def find_unique_rule(rules: dict, tickets: list):
    for pos in range(len(tickets[0].split(','))):
        unique_rule = None
        for r, _ in rules.items():
            # Check if rule applies for every ticket at current position 'pos'
            if all(rules[r](ticket.split(',')[pos]) for ticket in tickets):
                if unique_rule:  # If more then one rule applies to the position, skip the position
                    unique_rule = None
                    break
                unique_rule = (r, pos)
        # If unique rule was found, return it
        if unique_rule:
            return unique_rule


def load():
    data = problem.data()
    your_ticket = data.index('your ticket:')
    nearby_tickets = data.index('nearby tickets:')
    return [data[:your_ticket - 1], data[your_ticket + 1], data[nearby_tickets + 1:]]


if __name__ == '__main__':
    problem = Problem(16)
    data = load()

    rules = {(m := RULE_PATTERN.match(line)).group(1): _rule_closure(m.group(2), m.group(3), m.group(4), m.group(5))
             for line in data[0]}

    problem.submit(part_a(), 'a')  # 20091
    problem.submit(part_b(), 'b')  # 2325343130651
