#!/usr/bin/env python3

import numpy as np

with open("input.txt") as f:
    terrain = f.readlines()

n_trees = [0, 0, 0, 0, 0]

for idx, line in enumerate(terrain):
    for ii, slope in enumerate([1, 3, 5, 7]):
        if line[slope * idx % (len(line) - 1)] == "#":
            n_trees[ii] += 1

    if line[(idx // 2) % (len(line) - 1)] == "#" and idx % 2 == 0:
        n_trees[-1] += 1

print(n_trees)
print(np.prod(n_trees))
