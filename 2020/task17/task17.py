#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve

data = np.array(
    [
        [int(c) for c in line]
        for line in open("input.txt")
        .read()
        .replace(".", "0")
        .replace("#", "1")
        .splitlines()
    ],
    dtype=np.uint8,
)


def run_conway(inp, steps, dims):
    k = np.ones([3] * dims, dtype=np.uint8)
    k.ravel()[k.size // 2] = 0
    b = inp.reshape(*[[1] * (dims - inp.ndim) + list(inp.shape)])
    for _ in range(steps):
        c = convolve(b, k)
        b = np.pad(b, 1)
        b[:] = ((b == 1) & ((c == 2) | (c == 3))) | ((b == 0) & (c == 3))
    return b


print(np.sum(run_conway(data, 6, 3)))
print(np.sum(run_conway(data, 6, 4)))
