#!/usr/bin/env python3

from functools import reduce
from operator import mul
import re

rulemax = {"red": 12, "green": 13, "blue": 14}

lines = open("input.txt").read().splitlines()
total = 0
for line in lines:
    game, sets = line.split(":")
    possible = []
    for s in sets.split(";"):
        nums = map(int, re.findall(r"\d+", s))
        cols = re.findall(r"[a-z]+", s)
        results = dict(zip(cols, nums))
        possible.append(all(results[k] <= rulemax[k] for k in cols))
    if all(possible):
        total += int(re.findall(r"\d+", game)[0])
print(total)

powers = 0
for line in lines:
    results = {}
    for s in line.split(":")[1].split(";"):
        nums = map(int, re.findall(r"\d+", s))
        cols = re.findall(r"[a-z]+", s)
        for k, v in zip(cols, nums):
            results[k] = max(v, results.get(k, 0))
    powers += reduce(mul, results.values())
print(powers)
