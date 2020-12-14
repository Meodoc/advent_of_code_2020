from src.problem import Problem

from dataclasses import dataclass
import re

# Commands
UPDATE_MASK = 'mask'
STORE = 'mem'

PATTERNS = [re.compile(r'^(mask) = ([X|\d]+)'),
            re.compile(r'^(mem)\[(\d+)] = (\d+)')]


@dataclass
class Decoder:
    bitmask = [0, 0]
    memory = dict()

    def interpret(self, cmd, args) -> None:
        if cmd == UPDATE_MASK:
            self._update_mask(*args)
        elif cmd == STORE:
            self._store(*args)

    def _store(self, adr: int, val: int) -> None:
        self.memory[adr] = (int(val) | self.bitmask[0]) & self.bitmask[1]

    def _update_mask(self, mask: str) -> None:
        self.bitmask[0] = int(mask.replace('X', '0'), 2)
        self.bitmask[1] = int(mask.replace('X', '1'), 2)

    def calc_sum(self) -> int:
        return sum(self.memory.values())


def part_a():
    decoder = Decoder()
    for cmd, args in data:
        decoder.interpret(cmd, args)
    return decoder.calc_sum()


def part_b():
    return None


def load():
    return [(match.group(1), match.groups()[1:])
            for line in problem.data()
            for match in [p.match(line) for p in PATTERNS] if match]


if __name__ == '__main__':
    problem = Problem(14)
    data = load()

    print(part_a())
    problem.submit(part_a(), 'a')
    # problem.submit(part_b(), 'b')
