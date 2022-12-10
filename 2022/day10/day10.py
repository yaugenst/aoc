import textwrap

data = open("input.txt").read().strip()
data = data.replace("addx", "0").replace("noop", "0").replace("\n", " ")
instructions = map(int, data.split())

x = 1
part1 = 0
part2 = ""
for i, v in enumerate(instructions, 1):
    part1 += i * x if i % 40 == 20 else 0
    part2 += "#" if i % 40 in range(x, x + 3) else "."
    x += v
print(textwrap.fill(part2, 40))
print(part1)
