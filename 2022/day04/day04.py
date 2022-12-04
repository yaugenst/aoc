import re

data = open("input.txt").read().strip().split()

n = 0
for line in data:
    m = list(map(int, re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", line)[0]))
    a = range(m[0], m[1] + 1)
    b = range(m[2], m[3] + 1)

    # part 1
    if all([ai in b for ai in a]) or all([bi in a for bi in b]):
        n += 1

    # # part 2
    # if any([ai in b for ai in a]) or any([bi in a for bi in b]):
    #     n += 1
print(n)
