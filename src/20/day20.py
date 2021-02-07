from src.problem import Problem

from dataclasses import dataclass
from tqdm import tqdm
from enum import Enum

import numpy as np


class Axis(Enum):
    HORIZONTAL = 0,
    VERTICAL = 1


@dataclass
class Tile:
    id: int
    data: np.ndarray
    left, right, up, down = None, None, None, None

    def rotate_left(self):
        self.data = np.rot90(self.data)

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

    def __hash__(self):
        return hash(self.id)


class Image:
    head: Tile
    edge_tiles: set[Tile]
    tiles: np.ndarray
    data: np.ndarray

    def construct(self, tiles: list[Tile]):
        self.head = tiles[0]
        self.edge_tiles = {self.head}
        progress = tqdm(total=len(tiles), desc="Image construction")
        while len(tiles) > 0:
            for tile in tiles:
                if self.match(tile):
                    tiles.remove(tile)
                    progress.update()
        self.tiles, self.data = self.arrayify()

    def match(self, tile: Tile):
        for edge_tile in self.edge_tiles.copy():
            if self.try_match(edge_tile, tile):  # try to match the tile with every edge
                self.edge_tiles.add(tile)  # TODO: why does this only work when this loc is exactly here
                # TODO: when tile has matched with particular rotation, it should match with all the others whithout having to be rotated
                if not edge_tile.has_free_edge():
                    self.edge_tiles.remove(edge_tile)
        return tile.is_connected()

    def arrayify(self):
        curr = self.head
        while curr.left:  # find top left item
            curr = curr.left
        while curr.up:
            curr = curr.up
        tiled_image = None
        data = None
        while curr:  # traverse linked tiles and create tile and data arrays
            left = curr
            tile_row = np.array([])
            data_row = None
            while curr:
                if curr.has_free_edge() and curr not in self.edge_tiles:
                    raise RuntimeError("Incorrect tile assembly: inner image tiles contain empty links")
                tile_row = np.append(tile_row, curr)
                data_row = np.block([data_row, curr.data[1:-1, 1:-1]]) if data_row is not None else curr.data[1:-1, 1:-1]
                curr = curr.right
            tiled_image = np.block([[tiled_image], [tile_row]]) if tiled_image is not None else tile_row
            data = np.block([[data], [data_row]]) if data is not None else data_row
            curr = left.down
        return tiled_image, data

    def find_monsters(self):
        def _find_tail(d: np.ndarray, l: int, start: int):
            for i in range(start, len(d) - 1):
                if d[l+1, i] == '#' and d[l+2, i+1] == '#':
                    return [(l+1, i), (l+2, i+1)], i+2
            return None, len(d)

        def _find_body(d: np.ndarray, l: int, start: int):
            for i in range(start, len(d) - 3):
                if d[l+2, i] == '#' and d[l+1, i+1] == '#' and d[l+1, i+2] == '#' and d[l+2, i+3] == '#':
                    return [(l+2, i), (l+1, i+1), (l+1, i+2), (l+2, i+3)], i+4
            return None, len(d)

        def _find_head(d: np.ndarray, l: int, start: int):
            for i in range(start, len(d) - 3):
                if d[l+2, i] == '#' and d[l+1, i+1] == '#' and d[l+1, i+2] == '#' and d[l, i+2] == '#' and d[l+1, i+3] == '#':
                    return [(l+2, i), (l+1, i+1), (l+1, i+2), (l, i+2), (l+1, i+3)]
            return None

        max_monster_count = 0
        max_monsters = None
        for _ in range(2):  # vertical flips
            for _ in range(2):  # horizontal flips
                for _ in range(4):  # rotations
                    monsters = 0
                    data = self.data.copy()
                    for l in range(len(self.data) - 2):
                        tail, i = _find_tail(data, l, 0)
                        body1, i = _find_body(data, l, i)
                        body2, i = _find_body(data, l, i)
                        head = _find_head(data, l, i)
                        if head is not None:
                            for c in tail + body1 + body2 + head:
                                data[c[0], c[1]] = '0'
                                monsters += 1
                    if monsters > max_monster_count:
                        max_monster_count = monsters
                        max_monsters = data
                    self.data = np.rot90(self.data)
                self.data = np.flipud(self.data)
            self.data = np.fliplr(self.data)
        return max_monsters

    @staticmethod
    def try_match(edge_tile: Tile, tile: Tile):
        for _ in range(2):  # vertical flips
            for _ in range(2):  # horizontal flips
                for _ in range(4):  # rotations
                    if edge_tile.left_edge() is not None and np.array_equal(edge_tile.left_edge(), tile.right_edge()):
                        edge_tile.left = tile
                        tile.right = edge_tile
                        return True
                    if edge_tile.right_edge() is not None and np.array_equal(edge_tile.right_edge(), tile.left_edge()):
                        edge_tile.right = tile
                        tile.left = edge_tile
                        return True
                    if edge_tile.top_edge() is not None and np.array_equal(edge_tile.top_edge(), tile.bottom_edge()):
                        edge_tile.up = tile
                        tile.down = edge_tile
                        return True
                    if edge_tile.bottom_edge() is not None and np.array_equal(edge_tile.bottom_edge(), tile.top_edge()):
                        edge_tile.down = tile
                        tile.up = edge_tile
                        return True
                    tile.rotate_left()
                tile.flip(Axis.HORIZONTAL)
            tile.flip(Axis.VERTICAL)
        return False


def part_a(data: list):
    image = Image()
    image.construct(data)
    return image.tiles[0, 0].id * image.tiles[0, -1].id * image.tiles[-1, 0].id * image.tiles[-1, -1].id


def part_b(data: list):
    image = Image()
    image.construct(data)
    data = image.find_monsters()
    return np.count_nonzero(data == '#')


def load(p: Problem):
    return [Tile(int(tile.split('\n')[0].split(' ')[1][:-1]), np.array([np.array(list(l)) for l in tile.split('\n')[1:]]))
            for tile in p.raw_data().split('\n\n')]


if __name__ == '__main__':
    problem = Problem(20)

    #print(part_a(load(problem)))
    print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')  # 17032646100079
    # problem.submit(part_b(load(problem)), 'b')  # 2111 too high
