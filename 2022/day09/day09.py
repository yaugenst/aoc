data = open("input.txt").read().strip().split("\n")

rope = [0 + 0j] * 2  # * 10 for part 2
moves = {"L": -1j, "R": 1j, "U": 1, "D": -1}
hist = set(rope)

for line in data:
    m, n = line[0], int(line[2:])
    for _ in range(n):
        rope[0] += moves[m]
        for i in range(1, len(rope)):
            if abs((d := rope[i - 1] - rope[i])) >= 2:
                move = int(d.real / 2) + 1j * int(d.imag / 2)
                rope[i] = rope[i - 1] - move
        hist.add(rope[-1])

print(len(hist))
