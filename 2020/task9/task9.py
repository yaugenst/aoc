#!/usr/bin/env python3

import numpy as np

x = np.loadtxt("input.txt", dtype=int)
len_preamble = 25

def pairwise_sums(x):
    n, m = np.triu_indices(len(x), 1)
    pairs = np.vstack([x[n], x[m]]).T
    return pairs.sum(-1)

for i, n in enumerate(x[len_preamble:]):
    if n not in pairwise_sums(x[i:i+len_preamble]):
        print(n)
        break

for i in range(len(x)):
    for j in range(i+2, len(x)):
        if n == np.sum((r := x[i:j])):
            print(r.min() + r.max())
            exit()
