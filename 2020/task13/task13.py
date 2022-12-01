#!/usr/bin/env python3

fp = "input.txt"
t0, ids = open(fp).read().splitlines()
t0 = int(t0)
buses = [[idx, int(b)] for idx, b in enumerate(ids.split(",")) if b != "x"]


def check(t, t0, ids):
    return [(t - t0) * b for _, b in ids if not t % b]


t = t0
while not (r := check(t, t0, buses)):
    t += 1
print(r)


def update(t, idx, step, ids):
    delta, bus = ids[idx]
    if (t + delta) % bus == 0:
        return t, idx + 1, step * bus
    return t + step, idx, step


t = 0
idx = 1
step = buses[0][1]
while idx < len(buses):
    t, idx, step = update(t, idx, step, buses)
print(t)
