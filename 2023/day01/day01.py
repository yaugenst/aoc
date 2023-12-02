#!/usr/bin/env python3

import re

lines = open("input.txt").read().splitlines()

part1 = sum(
    map(lambda x: int(x[0] + x[-1]), (re.findall(r"\d", line) for line in lines))
)

print(part1)

stoi = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
rgx = r"(?=(\d|" + "|".join(stoi.keys()) + "))"

part2 = sum(
    map(
        lambda x: int(x[0] + x[-1]),
        ([stoi.get(m, m) for m in re.findall(rgx, ln)] for ln in lines),
    )
)

print(part2)
