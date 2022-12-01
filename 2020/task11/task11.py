#!/usr/bin/env python3

import numpy as np

fp = "input.txt"
data = np.asarray([list(line) for line in np.loadtxt(fp, dtype=str)])


def step(d, rule, n_ok):
    _d = np.pad(d, 1)
    _d1 = np.copy(_d)
    for idx, l in np.ndenumerate(d):
        x, y = (idx[0] + 1, idx[1] + 1)
        nb = rule(_d1, x, y)
        if d[idx] == "L" and "#" not in nb:
            _d[x, y] = "#"
        if d[idx] == "#" and nb.count("#") >= n_ok:
            _d[x, y] = "L"
    return _d[1:-1, 1:-1]


def rule_task1(d, x, y):
    nb = np.copy(d[x - 1 : x + 2, y - 1 : y + 2])
    nb[1, 1] = ""
    return "".join(nb.ravel())


def rule_task2(d, x, y):
    nb = first_neighbors(d[:, y], x)
    nb += first_neighbors(d[x, :], y)
    diag, adiag = get_diags(d, x, y)
    nb += first_neighbors(diag, min(x, y))
    nb += first_neighbors(adiag, min(x, d.shape[0] - 1 - y))
    return nb


def get_diags(a, row, col):
    nx, ny = a.shape
    adiag0 = (row + col - nx + 1, nx - 1) if row + col >= nx else (0, row + col)
    diag0 = (row - col, 0) if row > col else (0, col - row)
    r, c = [np.ravel_multi_index(i, a.shape) for i in [diag0, adiag0]]
    return (
        a.ravel()[r : r + (nx - diag0[0] - diag0[1]) * (ny + 1) : ny + 1],
        a.ravel()[c : c * (nx + 1) : ny - 1],
    )


def first_neighbors(x, idx, valid=["L", "#"]):
    _x = "".join(x)
    lr = [_x[:idx][::-1], _x[idx + 1 :]]
    ilr = [[f for s in valid if (f := _lr.find(s)) >= 0] for _lr in lr]
    return "".join([_lr[min(_ilr)] for _lr, _ilr in zip(lr, ilr) if len(_ilr) > 0])

d = np.copy(data)
while not np.array_equal(r := step(d, rule_task1, 4), d):
    d = r
print("".join(list(r.ravel())).count("#"))

d = np.copy(data)
while not np.array_equal(r := step(d, rule_task2, 5), d):
    d = r
print("".join(list(r.ravel())).count("#"))
