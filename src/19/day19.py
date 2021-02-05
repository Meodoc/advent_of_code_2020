from src.problem import Problem

import re
from itertools import product

RULE_PATTERN = re.compile(r'^(\d+): (?:([\d ]+)(?: \| ([\d ]+))?|\"([ab]+)\")$')


def part_a(data: dict):
    return sum(parse(data["rules"], msg) for msg in data["messages"])


def part_b(data: dict):
    valid = 0
    for msg in data["messages"]:
        for n_8, n_11 in product(range(10), repeat=2):
            patch_rules(data, n_8, n_11)
            if parse(data["rules"], msg):
                valid += 1
    return valid


def parse(rules: dict, msg: str):
    def _parse(rule: int, tokens: str):
        if rules[rule] in ['a', 'b']:
            try:
                return tokens[0] == rules[rule], 1
            except IndexError:
                return False, 1

        for opt in rules[rule]:
            accept = False
            pos = 0
            for subrule in opt:
                accept, r = _parse(subrule, tokens[pos:])
                pos += r
                if not accept:
                    break
            if accept:
                return True, pos
        return False, 0

    s, read = _parse(0, msg)
    return s if read == len(msg) else False


def patch_rules(data: dict, n_8: int, n_11: int):
    data["rules"][8] = [[42] + [42] * n_8]
    data["rules"][11] = [[42] + [42] * n_11 + [31] * n_11 + [31]]


def load(p: Problem):
    data = p.raw_data().split('\n\n')
    rules = {}
    for line in data[0].split('\n'):
        match = RULE_PATTERN.match(line)
        rules[int(match.group(1))] = match.group(4) if match.group(4) else [[int(r) for r in opt.split(' ')] for opt in
                                                                            match.groups()[1:] if opt]
    return {"rules": rules, "messages": data[1].split('\n')}


if __name__ == '__main__':
    problem = Problem(19)

    problem.submit(part_a(load(problem)), 'a')  # 156
    problem.submit(part_b(load(problem)), 'b')  # 363
