#!/usr/bin/env python3

with open("input.txt") as f:
    content = f.read().split("\n\n")
content = [l.removesuffix("\n").split("\n") for l in content]

print(sum([len(set("".join(l))) for l in content]))
print(sum([len(set.intersection(*[set(li) for li in l])) for l in content]))
