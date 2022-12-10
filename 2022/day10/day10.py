data = open("input.txt").read().strip().split("\n")
cycles = {"addx": 2, "noop": 1}

x = 1
cycle = 1
result = 0
for line in data:
    for _ in range(cycles[line[:4]]):
        if cycle == 20 or (cycle + 20) % 40 == 0:
            result += x * cycle
        cycle += 1
    if line[:4] == "addx":
        x += int(line[5:])
print(result)
