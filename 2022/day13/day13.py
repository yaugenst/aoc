from functools import cmp_to_key
from math import prod


def compare(a, b):
    match a, b:
        case int(), int():
            return (a < b) - (a > b)
        case list(), list():
            for ai, bi in zip(a, b):
                if (x := compare(ai, bi)) != 0:
                    return x
            return compare(len(a), len(b))
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])


data = open("input.txt").read().strip().split("\n\n")
data = [list(map(eval, x.split("\n"))) for x in data]

print(sum(i for i, ab in enumerate(data, 1) if compare(*ab) == 1))

part2 = sorted(sum(data, div := [[2], [6]]), key=cmp_to_key(compare), reverse=True)
print(prod(i for i, a in enumerate(part2, 1) if a in div))
