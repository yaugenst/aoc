#!/usr/bin/env python3

import numpy as np

fp = "input.txt"
joltage = np.loadtxt(fp, dtype=int)
joltage.sort()
joltage = np.array([0] + list(joltage) + [joltage[-1] + 3])


def valid(x, j, res):
    if len(j) == 0:
        return
    idx = np.abs(j - x) <= 3
    res += list(j[idx])
    valid(res[-1], j[~idx], res)


res = []
valid(0, joltage, res)
unique, counts = np.unique(np.diff(res), return_counts=True)
print(np.prod(counts))

ways = {0: 1}
for j in joltage[1:]:
    ways[j] = sum([ways.get(j - diff, 0) for diff in [1, 2, 3]])
print(ways[joltage[-1]])
