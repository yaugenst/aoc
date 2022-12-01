#!/usr/bin/env python3

import numpy as np

x = np.loadtxt("input.txt", dtype=int)
n, m = np.triu_indices(len(x), 1)
pairs = np.vstack([x[n], x[m]]).T
sums = pairs.sum(-1)
print(np.prod(pairs[sums == 2020]))

triplets = np.array(np.meshgrid(sums, x)).T.reshape(-1, 2)
print(np.prod(triplets[triplets.sum(-1) == 2020].T[1]))
