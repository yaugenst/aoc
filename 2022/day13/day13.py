from functools import cmp_to_key, reduce


def cmp(*n):
    if all(isinstance(x, int) for x in n):
        return n[0] - n[1]
    elif not all(isinstance(x, list) for x in n):
        return cmp(*[[x] if isinstance(x, int) else x for x in n])
    return x if (x := next((x for x in map(cmp, *n) if x), 0)) else cmp(*map(len, n))


p1 = [[*map(eval, x.split())] for x in open("input.txt").read().split("\n\n")]
print(sum(i for i, ab in enumerate(p1, 1) if cmp(*ab) < 0))
p2 = sorted(sum(p1, div := [[2], [6]]), key=cmp_to_key(cmp))
print(reduce(lambda x, y: x * y, [p2.index(v) + 1 for v in div]))
