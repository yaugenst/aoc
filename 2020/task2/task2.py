#!/usr/bin/env python3
import re

with open("input.txt") as f:
    content = f.readlines()
expr = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
num_valid = [0, 0]
for line in content:
    lo, hi, letter, word = expr.findall(line)[0]
    if int(lo) <= word.count(letter) <= int(hi):
        num_valid[0] += 1
    if (word[int(lo) - 1] == letter) ^ (word[int(hi) - 1] == letter):
        num_valid[1] += 1
print(num_valid)
