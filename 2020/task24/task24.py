#!/usr/bin/env python3

import re
from collections import defaultdict

dirs = {
    "ne": 1 + 1j,
    "e": 2 + 0j,
    "se": 1 - 1j,
    "sw": -1 - 1j,
    "w": -2 + 0j,
    "nw": -1 + 1j,
}

tiles = open("input.txt").readlines()
flips = defaultdict(int)
for tile in tiles:
    flips[sum(dirs[d] for d in re.findall(r"([ns]?[ew])", tile))] += 1
blacks = {k for k, v in flips.items() if v % 2}
print(len(blacks))

for _ in range(100):
    adjacent = defaultdict(int)
    for coordinate in blacks:
        for c in [coordinate + t for t in dirs.values()]:
            adjacent[c] += 1
    blacks = {c for c, n in adjacent.items() if (c in blacks and n == 1) or n == 2}
print(len(blacks))
