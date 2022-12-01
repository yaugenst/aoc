#!/usr/bin/env python3

import re

fp = "input.txt"
instructions = re.findall(r"(\w)(\d+)", open(fp).read())
moveset = {
    "N": lambda x, r, v: (x + v * (+0 + 1j), r),
    "E": lambda x, r, v: (x + v * (+1 + 0j), r),
    "S": lambda x, r, v: (x + v * (+0 - 1j), r),
    "W": lambda x, r, v: (x + v * (-1 + 0j), r),
    "F": lambda x, r, v: (x + v * r, r),
    "L": lambda x, r, v: (x, r * 1j ** (v // 90)),
    "R": lambda x, r, v: (x, r / 1j ** (v // 90)),
}

x = 0 + 0j
r = 1 + 0j
for k, v in instructions:
    x, r = moveset[k](x, r, int(v))
print(abs(x.real) + abs(x.imag))

x = 0 + 0j
w = 10 + 1j
for k, v in instructions:
    if k == "F":
        x = moveset[k](x, w, int(v))[0]
    else:
        w = moveset[k](w, w, int(v))[0 if k in "NESW" else 1]
print(abs(x.real) + abs(x.imag))
