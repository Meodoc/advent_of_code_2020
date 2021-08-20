from __future__ import annotations
from src.problem import Problem
from dataclasses import dataclass, field
from collections import defaultdict
from copy import deepcopy
import re
import funcy

WHITE, BLACK = False, True
PATTERN = re.compile('e|se|sw|w|nw|ne')
DIRECTIONS = {'e': lambda x, y: (x + 1, y),
              'se': lambda x, y: (x + 1, y - 1),
              'sw': lambda x, y: (x, y - 1),
              'w': lambda x, y: (x - 1, y),
              'nw': lambda x, y: (x - 1, y + 1),
              'ne': lambda x, y: (x, y + 1)}


@dataclass(unsafe_hash=True)
class Tile:
    state = WHITE
    pos: tuple

    def flip(self) -> None:
        self.state = not self.state

    def is_adj(self, x: int, y: int):
        return abs(self.pos[0] - x) <= 1 and abs(self.pos[1] - y) <= 1 and \
               (self.pos[0] + 1, self.pos[1] + 1) != (x, y) and \
               (self.pos[0] - 1, self.pos[1] - 1) != (x, y) and \
               self.pos != (x, y)

    def adj_indices(self) -> list:
        return [(self.pos[0] + 1, self.pos[1]), (self.pos[0], self.pos[1] + 1), (self.pos[0] - 1, self.pos[1]),
                (self.pos[0], self.pos[1] - 1), (self.pos[0] + 1, self.pos[1] - 1), (self.pos[0] - 1, self.pos[1] + 1)]


class HexGrid:
    tiles = {(0, 0): Tile((0, 0))}

    def find_and_flip(self, instructions: list) -> None:
        for instr in instructions:
            x, y = 0, 0
            for dir_ in instr:
                x, y = self.apply_direction(dir_, x, y)
            tile = Tile((x, y))
            if (x, y) not in self.tiles:
                self.tiles[(x, y)] = tile
            for adj in tile.adj_indices():
                if adj not in self.tiles:
                    self.tiles[adj] = Tile(adj)
            self.tiles[(x, y)].flip()

    def live(self, iterations: int) -> None:
        for _ in range(iterations):
            nxt = deepcopy(self.tiles)
            for pos, tile in self.tiles.items():
                adj_black = self.count_color(BLACK, self.adj(tile))
                if tile.state == BLACK and (adj_black == 0 or adj_black > 2):
                    nxt[tile.pos].flip()
                elif tile.state == WHITE and adj_black == 2:
                    nxt_tile = nxt[tile.pos]
                    nxt_tile.flip()
                    for adj in nxt_tile.adj_indices():
                        if adj not in nxt:
                            nxt[adj] = Tile(adj)
            self.tiles = nxt
            print("Day", _ + 1, self.count_color(BLACK))

    @staticmethod
    def apply_direction(dir_: str, x: int, y: int) -> tuple:
        return DIRECTIONS[dir_](x, y)

    def count_color(self, color: bool, tiles: list = None) -> int:
        return len([tile for tile in (tiles if tiles else self.tiles.values()) if tile.state == color])

    def adj(self, ref: Tile) -> list:
        return [tile for tile in self.tiles.values() if tile.is_adj(*ref.pos)]


def part_a(instructions: list):
    hexgrid = HexGrid()
    hexgrid.find_and_flip(instructions)
    return hexgrid.count_color(BLACK)


def part_b(instructions: list):
    hexgrid = HexGrid()
    hexgrid.find_and_flip(instructions)
    print(hexgrid.count_color(BLACK))
    hexgrid.live(iterations=100)
    return None


def load(p: Problem):
    return [re.findall(PATTERN, instr) for instr in p.data()]


if __name__ == '__main__':
    problem = Problem(24, test=True)

    # print(part_a(load(problem)))
    print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
