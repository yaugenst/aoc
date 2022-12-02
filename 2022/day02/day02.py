data = open("input.txt").read()

points = {"X": 1, "Y": 2, "Z": 3}
beat = {"C": "X", "A": "Y", "B": "Z"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"B": "X", "C": "Y", "A": "Z"}

score = 0
for line in data.strip().split("\n"):
    a, b = line[0], line[2]

    # # uncomment for part 2
    # b = {"X": lose, "Y": draw, "Z": beat}[b][a]

    score += points[b]
    if b == draw[a]:
        score += 3
    if b == beat[a]:
        score += 6

print(score)
