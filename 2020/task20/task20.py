#!/usr/bin/env python3

import re
from copy import copy

import numpy as np


class Tile:
    def __init__(self, x):
        x = x.splitlines()
        self.id = int(re.findall(r"\d+", x[0])[0])
        self.data = np.array([list(xi) for xi in x[1:]])

    @property
    def borders(self):
        return {
            "u": self.data[0, :],
            "d": self.data[-1, :],
            "l": self.data[:, 0],
            "r": self.data[:, -1],
        }

    def rotations(self):
        for n in range(4):
            self.data = np.rot90(self.data, n)
            yield self

    def orientations(self):
        yield from self.rotations()
        self.data = np.flip(self.data, 0)
        yield from self.rotations()

    def __getitem__(self, key):
        return self.data[key]


class Grid:
    def __init__(self, shape):
        self.shape = shape
        self.indices = [xy for xy in np.ndindex(shape)]
        self.idx = 0
        self.tiles = np.empty(shape, dtype=np.object)

    def add(self, tile):
        for t in tile.orientations():
            if self.can_place(tile, self.indices[self.idx]):
                self.tiles[self.indices[self.idx]] = tile
                self.idx += 1
                return True
        return False

    def can_place(self, tile, idx):
        if idx[0] > 0 and not all(
            self.tiles[idx[0] - 1, idx[1]].borders["d"] == tile.borders["u"]
        ):
            return False
        if idx[1] > 0 and not all(
            self.tiles[idx[0], idx[1] - 1].borders["r"] == tile.borders["l"]
        ):
            return False
        return True

    @staticmethod
    def from_tiles(tiles):
        def assemble(grid, tiles):
            if not tiles:
                return grid
            for idx, tile in enumerate(tiles):
                if (g := copy(grid)).add(tile):
                    if result := assemble(g, tiles[:idx] + tiles[idx + 1 :]):
                        return result

        shape = tuple(2 * [int(np.sqrt(len(tiles)))])
        grid = Grid(shape)
        return assemble(grid, tiles)

    def to_numpy(self):
        rows = []
        for row in np.reshape(tuple(self.indices), (*self.shape, 2)):
            rows.append(
                np.concatenate([self.tiles[tuple(col)][1:-1, 1:-1] for col in row], 1)
            )
        return np.concatenate(rows, 0)


def mult_corners(grid):
    return np.prod([grid.tiles[idx].id for idx in [(0, 0), (0, -1), (-1, 0), (-1, -1)]])


def water_roughness(grid, monster):
    n = 0
    for row in range(grid.shape[0] - monster.shape[0]):
        for col in range(grid.shape[1] - monster.shape[1]):
            sub = grid[row : row + monster.shape[0], col : col + monster.shape[1]]
            n += np.all(sub[np.where(monster == "#")] == "#")
    if n > 0:
        return np.sum(grid == "#") - n * np.sum(monster == "#")


fp = "input.txt"
tiles = [Tile(x) for x in open(fp).read().split("\n\n")]
grid = Grid.from_tiles(tiles)
print(mult_corners(grid))

ngrid = grid.to_numpy()
monster = Tile(open("monster.txt").read())
for nessie in monster.orientations():
    if val := water_roughness(ngrid, nessie.data):
        print(val)
        break
