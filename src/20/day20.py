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
                    break
        self.tiles, self.data = self.arrayify()

    def match(self, tile: Tile):
        for edge_tile in self.edge_tiles.copy():
            if self.try_match(edge_tile, tile):  # try to match the tile with every edge
                self.edge_tiles.add(tile)
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
                    print(str(curr.id) + " yikes")
                tile_row = np.append(tile_row, curr)
                data_row = np.block([data_row, curr.data]) if data_row is not None else curr.data
                curr = curr.right
            tiled_image = np.block([[tiled_image], [tile_row]]) if tiled_image is not None else tile_row
            data = np.block([[data], [data_row]]) if data is not None else data_row
            curr = left.down
        return tiled_image, data

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
    return image.tiles[0][0].id * image.tiles[0][-1].id * image.tiles[-1][0].id * image.tiles[-1][-1].id


def part_b(data: list):
    return None


def load(p: Problem):
    return [Tile(int(tile.split('\n')[0].split(' ')[1][:-1]), np.array([np.array(list(l)) for l in tile.split('\n')[1:]]))
            for tile in p.raw_test_data().split('\n\n')]


if __name__ == '__main__':
    problem = Problem(20)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')  # 17032646100079
    # problem.submit(part_b(load(problem)), 'b')
