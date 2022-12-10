data = open("input.txt").read().strip().split("\n")
cycles = {"addx": 2, "noop": 1}

x = 1
cycle = 1
result = 0
nx = 40
for line in data:
    for _ in range(cycles[line[:4]]):
        # part 1
        if cycle == 20 or (cycle + 20) % 40 == 0:
            result += x * cycle

        # part 2
        c = "#" if cycle % nx in range(x, x + 3) else "."
        print(c, end="")
        if cycle % nx == 0:
            print()

        cycle += 1
    if line[:4] == "addx":
        x += int(line[5:])
print(result)
