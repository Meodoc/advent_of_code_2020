from src.problem import Problem

from copy import deepcopy
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

    # Algorithm uniquely identifies the rule for each field position and stores them in a dict:
    #  The algorithm searches for every position 'pos' a rule that uniquely applies to the position, meaning no other
    #  rule is allowed to apply to this position. Once such a rule is found, its position is certain and can therefore
    #  be added to the 'rule_positions' dict. Then the search for the next rule begins again from the position 0.
    #  The algorithm is finished once it finds a position for every rule.
    rule_positions = dict()
    while len(rule_positions) < (n_fields := len(data[1].split(','))):
        for pos in range(n_fields):
            applying_rule = None
            for r, _ in rules.items():
                # Check if rule applies for every ticket at current position 'pos'
                if all(rules[r](ticket.split(',')[pos]) for ticket in valid_tickets):
                    if applying_rule:  # If more then one rule applies to the position, skip this position for now
                        applying_rule = None
                        break
                    applying_rule = (r, pos)
            # If exactly one rule applies, save the position of that rule and remove it from the available rules
            if applying_rule:
                rule_positions[applying_rule[0]] = applying_rule[1]
                rules.pop(applying_rule[0])
                break

    # Returns the product of all fields in own ticket that start with 'departure'
    return prod(int(field) for pos, field in enumerate(data[1].split(',')) if pos in
                [r_pos for rule, r_pos in rule_positions.items() if rule.startswith('departure')])


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
