data = open("input.txt").read().strip().split("\n")

grid = []
for line in data:
    grid.append([int(x) for x in list(line)])

# part 1
visible = 2 * (len(grid) + len(grid[0]) - 2)
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        gij = grid[i][j]
        visible += (
            all(gij > g for g in grid[i][:j])
            | all(gij > g for g in grid[i][j + 1 :])
            | all(gij > g for g in (grid[k][j] for k in range(i)))
            | all(gij > g for g in (grid[k][j] for k in range(i + 1, len(grid[0]))))
        )
print(visible)

# part 2
scores = []
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        l = 0
        for g in grid[i][:j][::-1]:
            l += 1
            if g >= grid[i][j]:
                break
        r = 0
        for g in grid[i][j + 1 :]:
            r += 1
            if g >= grid[i][j]:
                break
        t = 0
        for g in [grid[k][j] for k in range(i)][::-1]:
            t += 1
            if g >= grid[i][j]:
                break
        b = 0
        for g in [grid[k][j] for k in range(i + 1, len(grid[0]))]:
            b += 1
            if g >= grid[i][j]:
                break
        scores.append(l * r * t * b)
print(max(scores))
