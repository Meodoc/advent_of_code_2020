from src.problem import Problem

from dataclasses import dataclass
from itertools import product
import re

# Commands
UPDATE_MASK = 'mask'
STORE = 'mem'

BITMASK_LEN = 36

PATTERNS = [re.compile(fr'^({UPDATE_MASK}) = ([X|\d]+)'),
            re.compile(fr'^({STORE})\[(\d+)] = (\d+)')]


@dataclass
class Decoder:
    bitmask = [0, 0]
    memory = dict()

    def interpret(self, cmd, args) -> None:
        if cmd == UPDATE_MASK:
            self._update_mask(*args)
        elif cmd == STORE:
            self._store(*args)

    def _store(self, adr: str, val: str) -> None:
        self.memory[adr] = (int(val) | self.bitmask[0]) & self.bitmask[1]

    def _update_mask(self, mask: str) -> None:
        self.bitmask[0] = int(mask.replace('X', '0'), 2)
        self.bitmask[1] = int(mask.replace('X', '1'), 2)

    def calc_sum(self) -> int:
        return sum(self.memory.values())


class QuantumDecoder(Decoder):
    bitmask: int
    q_indices: list

    def _store(self, adr: str, val: str) -> None:
        for p in product([0, 1], repeat=len(self.q_indices)):
            q_adr = self.int_to_bin_str(int(adr), BITMASK_LEN)
            for i in range(len(self.q_indices)):
                q_adr = self.replace_at_index(q_adr, str(p[i]), self.q_indices[i])
            q_adr = int(q_adr, 2) | self.bitmask
            self.memory[q_adr] = int(val)

    def _update_mask(self, mask: str) -> None:
        self.bitmask = int(mask.replace('X', '0'), 2)
        self.q_indices = [f.start() for f in re.finditer('X', mask)]

    @staticmethod
    def int_to_bin_str(val: int, l: int) -> str:
        return format(val, 'b').zfill(l)

    @staticmethod
    def replace_at_index(s: str, r: str, idx: int) -> str:
        return s[:idx] + r + s[idx + 1:]


def part_a():
    decoder = Decoder()
    for cmd, args in data:
        decoder.interpret(cmd, args)
    return decoder.calc_sum()


def part_b():
    decoder = QuantumDecoder()
    for cmd, args in data:
        decoder.interpret(cmd, args)
    return decoder.calc_sum()


def load():
    return [(match.group(1), match.groups()[1:])
            for line in problem.data()
            for match in [p.match(line) for p in PATTERNS] if match]


if __name__ == '__main__':
    problem = Problem(14)
    data = load()

    problem.submit(part_a(), 'a')  # 6513443633260
    problem.submit(part_b(), 'b')  # 3442819875191
