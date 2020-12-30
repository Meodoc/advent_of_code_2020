from src.problem import Problem

import re

RULE_PATTERN = re.compile(r'^(\d+): (?:([\d ]+)(?: \| ([\d ]+))?|\"([ab]+)\")$')


def part_a(data: dict):
    return sum(parse(data["rules"], msg) for msg in data["messages"])


def part_b(data: dict):
    data["rules"][8] = [[42], [42, 8]]
    data["rules"][11] = [[42, 31], [42, 11, 31]]
    return sum(parse_b(data["rules"], msg) for msg in data["messages"])


def parse(rules: dict, msg: str):
    def _parse(rule: int, tokens: str):
        if rules[rule] in ['a', 'b']:
            return tokens[0] == rules[rule], 1

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

def parse_b(rules: dict, msg: str):
    def _parse(rule: int, tokens: str):
        if rules[rule] in ['a', 'b']:
            return tokens[0] == rules[rule], 1

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
    print(s, msg)
    return s if read == len(msg) else False


def load(p: Problem):
    data = p.raw_test_data().split('\n\n')
    rules = {}
    for line in data[0].split('\n'):
        match = RULE_PATTERN.match(line)
        rules[int(match.group(1))] = match.group(4) if match.group(4) else [[int(r) for r in opt.split(' ')] for opt in
                                                                            match.groups()[1:] if opt]
    return {"rules": rules, "messages": data[1].split('\n')}


if __name__ == '__main__':
    problem = Problem(19)

    #print(part_a(load(problem)))
    print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')  # 156
    # problem.submit(part_b(load()), 'b')
