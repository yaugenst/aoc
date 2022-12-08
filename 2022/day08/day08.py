data = open("input.txt").read().strip().split("\n")

grid = []
for line in data:
    grid.append([int(x) for x in list(line)])

visible = 2 * (len(grid) + len(grid[0]) - 2)
scores = []
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        v = False
        scores.append(1)
        for search_direction in [
            grid[i][:j][::-1],
            grid[i][j + 1 :],
            [grid[k][j] for k in range(i)][::-1],
            [grid[k][j] for k in range(i + 1, len(grid[0]))],
        ]:
            # part 1
            v |= all(grid[i][j] > g for g in search_direction)

            # part 2
            score = 0
            for tree in search_direction:
                score += 1
                if tree >= grid[i][j]:
                    break
            scores[-1] *= score
        visible += v
print(visible)
print(max(scores))
