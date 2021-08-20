from __future__ import annotations
from src.problem import Problem
from dataclasses import dataclass, field
from collections import defaultdict
import re
import funcy

WHITE, BLACK = False, True
PATTERN = re.compile('e|se|sw|w|nw|ne')


@dataclass(unsafe_hash=True)
class Tile:
    state = WHITE
    pos: tuple

    def flip(self) -> None:
        self.state = not self.state


class HexGrid:
    tiles = {Tile((0, 0))}

    def find_and_flip(self, instructions: list) -> None:
        # e, se, sw, w, nw, and ne
        for instruction in instructions:
            x, y = 0, 0
            for direction in instruction:
                if direction == 'e':
                    x += 1
                elif direction == 'se':
                    x += 1
                    y -= 1
                elif direction == 'sw':
                    y -= 1
                elif direction == 'w':
                    x -= 1
                elif direction == 'nw':
                    x -= 1
                    y += 1
                elif direction == 'ne':
                    y += 1
            self.tiles.add(Tile((x, y)))
            for tile in self.tiles:
                if tile.pos == (x, y):
                    tile.flip()
                    break
            # list(tile for tile in self.tiles if tile.pos == (x, y))[0].flip()

    def count(self, color: bool):
        return len([tile for tile in self.tiles if tile.state == color])


def part_a(instructions: list):
    hexgrid = HexGrid()
    hexgrid.find_and_flip(instructions)
    return hexgrid.count(BLACK)


def part_b(data: list):
    return None


def load(p: Problem):
    return [re.findall(PATTERN, instr) for instr in p.data()]


if __name__ == '__main__':
    problem = Problem(24, test=True)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
