#!/usr/bin/env python3


def run(data, task):
    res = {}
    for lhs, rhs in data:
        if lhs == "mask":
            mask = rhs
            continue
        task(int(lhs[4:-1]), int(rhs), mask, res)
    print(sum(res.values()))


def task1(adr, val, mask, res):
    val &= int(mask.replace("X", "1"), 2)
    val |= int(mask.replace("X", "0"), 2)
    res[adr] = val


def task2(adr, val, mask, res):
    candidates = [adr | int(mask.replace("X", "0"), 2)]
    m = 1
    for char in mask[::-1]:
        if char == "X":
            candidates = [
                f(c) for c in candidates for f in (lambda x: x & ~m, lambda x: x | m)
            ]
        m <<= 1
    for a in candidates:
        res[a] = val


if __name__ == "__main__":
    fp = "input.txt"
    data = [l.split(" = ") for line in open(fp).readlines() if (l := line.strip())]
    run(data, task1)
    run(data, task2)
