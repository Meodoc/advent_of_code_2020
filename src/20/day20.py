from dataclasses import dataclass

from src.problem import Problem

import numpy as np
from enum import Enum


class Dir(Enum):
    LEFT = 0,
    RIGHT = 1,
    UP = 3,
    DOWN = 4,
    NONE = 5


class Axis(Enum):
    HORIZONTAL = 0,
    VERTICAL = 1


@dataclass
class Tile:
    id: int
    data: np.ndarray
    left, right, up, down = None, None, None, None

    def rotate(self, direction: Dir):
        if direction == Dir.LEFT:
            self.data = np.rot90(self.data)
        elif direction == Dir.RIGHT:
            self.data = np.rot90(self.data, k=3)
        else:
            raise ValueError()

    def flip(self, axis: Axis):
        if axis == Axis.HORIZONTAL:
            self.data = np.flipud(self.data)
        elif axis == Axis.VERTICAL:
            self.data = np.fliplr(self.data)
        else:
            raise ValueError()

    def is_connected(self):
        return self.left or self.right or self.up or self.down

    def has_free_edge(self):
        return not self.left or not self.right or not self.up or not self.down

    def left_edge(self):
        return self.data[:, 0] if not self.left else None

    def right_edge(self):
        return self.data[:, -1] if not self.right else None

    def top_edge(self):
        return self.data[0, :] if not self.up else None

    def bottom_edge(self):
        return self.data[-1, :] if not self.down else None


class Image:
    def __init__(self, head: Tile):
        self.head = head
        self.edge_tiles = [head]

    def match_backup(self, tile: Tile):
        for edge_tile in self.edge_tiles:
            if self.try_match(edge_tile, tile):
                self.edge_tiles.append(tile)
                if not edge_tile.has_free_edge():
                    self.edge_tiles.remove(edge_tile)
                return True
        return False

    def match(self, tile: Tile):
        for edge_tile in self.edge_tiles:
            if self.try_match(edge_tile, tile):
                self.edge_tiles.append(tile)
                if not edge_tile.has_free_edge():
                    self.edge_tiles.remove(edge_tile)

        if tile.is_connected():
            return True
        return False

    def arrayify(self):
        curr = self.edge_tiles[0]
        while curr.left:
            curr = curr.left
        while curr.up:
            curr = curr.up
        image = []
        while curr:
            left = curr
            line = []
            while curr:
                line.append(curr)
                curr = curr.right
            image.append(line)
            curr = left.down
        return image

    @staticmethod
    def try_match(edge_tile: Tile, tile: Tile):
        if edge_tile.left_edge() is not None:
            for _ in range(2):
                for _ in range(2):
                    for _ in range(4):
                        if np.array_equal(edge_tile.left_edge(), tile.right_edge()):
                            edge_tile.left = tile
                            tile.right = edge_tile
                            return True
                        tile.rotate(Dir.LEFT)
                    tile.flip(Axis.HORIZONTAL)
                tile.flip(Axis.VERTICAL)

        if edge_tile.right_edge() is not None:
            for _ in range(2):
                for _ in range(2):
                    for _ in range(4):
                        if np.array_equal(edge_tile.right_edge(), tile.left_edge()):
                            edge_tile.right = tile
                            tile.left = edge_tile
                            return True
                        tile.rotate(Dir.LEFT)
                    tile.flip(Axis.HORIZONTAL)
                tile.flip(Axis.VERTICAL)

        if edge_tile.top_edge() is not None:
            for _ in range(2):
                for _ in range(2):
                    for _ in range(4):
                        if np.array_equal(edge_tile.top_edge(), tile.bottom_edge()):
                            edge_tile.up = tile
                            tile.down = edge_tile
                            return True
                        tile.rotate(Dir.LEFT)
                    tile.flip(Axis.HORIZONTAL)
                tile.flip(Axis.VERTICAL)

        if edge_tile.bottom_edge() is not None:
            for _ in range(2):
                for _ in range(2):
                    for _ in range(4):
                        if np.array_equal(edge_tile.bottom_edge(), tile.top_edge()):
                            edge_tile.down = tile
                            tile.up = edge_tile
                            return True
                        tile.rotate(Dir.LEFT)
                    tile.flip(Axis.HORIZONTAL)
                tile.flip(Axis.VERTICAL)
        return False


def part_a(data: list):
    image = Image(data[0])
    data.remove(data[0])
    while len(data) > 0:
        for tile in data:
            if image.match(tile):
                data.remove(tile)
                break
    image_data = image.arrayify()
    return image_data[0][0].id * image_data[0][-1].id * image_data[-1][0].id * image_data[-1][-1].id


def part_b(data: list):
    return None


def load(p: Problem):
    return [Tile(int(tile.split('\n')[0].split(' ')[1][:-1]), np.array([np.array(list(l)) for l in tile.split('\n')[1:]]))
            for tile in p.raw_data().split('\n\n')]


if __name__ == '__main__':
    problem = Problem(20)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
