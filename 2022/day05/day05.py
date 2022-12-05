import re

stacks, moves = open("input.txt").read().split("\n\n")

sd = {k: [] for k in map(int, re.findall(r"\d+", stacks.split("\n")[-1]))}
for line in stacks.split("\n")[:-1]:
    for n, idx in enumerate(range(1, len(line), 4)):
        if line[idx] != " ":
            sd[n + 1].append(line[idx])

for move in moves.split("\n"):
    a, b, c = map(int, re.findall(r"\d+", move))

    # part 1
    sd[c] = [sd[b].pop(0) for _ in range(a)][::-1] + sd[c]

    # # part 2
    # sd[c] = [sd[b].pop(0) for _ in range(a)] + sd[c]
print("".join([v[0] for v in sd.values()]))
