#!/usr/bin/env python3

passes = [line.rstrip() for line in open("input.txt")]


def bs(x, lo, hi, s):
    c = (lo + hi) // 2
    if not x:
        return c
    return bs(x[1:], lo, c, s) if x[0] == s else bs(x[1:], c + 1, hi, s)


seat_ids = [8 * bs(p[:-3], 0, 127, "F") + bs(p[-3:], 0, 7, "L") for p in passes]
seat_ids.sort()

print(seat_ids[-1])
print([x for x in range(seat_ids[0], seat_ids[-1] + 1) if x not in seat_ids])
