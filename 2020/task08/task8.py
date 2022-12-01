#!/usr/bin/env python3

import re

expr = re.compile(r"(\w+) ([+,-]?\d+)")
code = []
for idx, line in enumerate(open("input.txt")):
    instr, val = expr.findall(line)[0]
    code.append([instr, int(val), True])

def run(c, idx, acc, onlyfirst=True):
    if idx == len(c) and not onlyfirst:
        return acc

    instr, val, firstrun = c[idx]

    if not firstrun and onlyfirst:
        return acc

    c[idx][2] = False
    if instr == "acc":
        acc += val
    if instr == "jmp":
        idx += val
    else:
        idx += 1

    return run(c, idx, acc, onlyfirst)

print(run(code, 0, 0, True))

for idx, (instr, val, _) in enumerate(code):
    if instr in ["jmp", "nop"]:
        for instr in ["jmp", "nop"]:
            test = [l.copy() for l in code]
            test[idx][0] = instr
            try:
                print(run(test, 0, 0, False))
                break
            except:
                continue
