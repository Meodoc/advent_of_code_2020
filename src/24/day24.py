from __future__ import annotations
from src.problem import Problem
from dataclasses import dataclass, field
from collections import defaultdict
import re

PATTERN = re.compile('e|se|sw|w|nw|ne')
WHITE, BLACK = False, True


class Tile:
    state = WHITE
    neigh = defaultdict(lambda: Tile())

    def flip(self):
        self.state = not self.state


class HexGrid:
    _start = Tile()

    def flip(self, instr: list):
        dest = self._traverse(instr)
        dest.flip()

    def _traverse(self, instr: list):
        cur = self._start
        for d in instr:
            nxt = cur.neigh[d]
            nxt.neigh[self.adj(d)] = cur
            cur = nxt
        return cur

    @staticmethod
    def adj(d: str):
        return d.translate(str.maketrans('nesw', 'swne'))


def part_a(instr: list):
    hexgrid = HexGrid()
    hexgrid.flip(instr[0])

    return None


def part_b(data: list):
    return None


def load(p: Problem):
    return [re.findall(PATTERN, instr) for instr in p.test_data()]


if __name__ == '__main__':
    problem = Problem(24)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
