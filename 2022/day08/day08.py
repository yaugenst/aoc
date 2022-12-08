data = open("input.txt").read().strip().split("\n")

grid = []
for line in data:
    grid.append([int(x) for x in list(line)])
print(grid)

scores = []
visible = 2 * len(grid) + 2 * len(grid[0]) - 4
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        l = 0
        for ii, g in enumerate(grid[i][:j][::-1]):
            l += 1
            if g >= grid[i][j]:
                break
        r = 0

        for ii, g in enumerate(grid[i][j + 1 :]):
            r += 1
            if g >= grid[i][j]:
                break
        t = 0
        for ii, g in enumerate([grid[k][j] for k in range(i)][::-1]):
            t += 1
            if g >= grid[i][j]:
                break
        b = 0
        for ii, g in enumerate([grid[k][j] for k in range(i + 1, len(grid[0]))]):
            b += 1
            if g >= grid[i][j]:
                break
        scores.append(l * r * t * b)
        # exit()
        # h = all(grid[i][j] > g for g in grid[i][:j]) or all(
        #     grid[i][j] > g for g in grid[i][j + 1 :]
        # )
        # v = all(grid[i][j] > g for g in [grid[k][j] for k in range(i)]) or all(
        #     grid[i][j] > g for g in [grid[k][j] for k in range(i + 1, len(grid[0]))]
        # )
        # print(i, j)
        # print(list(range(j)))
        # print([g for g in [grid[k][j] for k in range(i)]])
        # print([g for g in [grid[k][j] for k in range(i + 1, len(grid[0]))]])
        # continue
        # exit()
        # # print([grid[i][j] > g for g in [grid[k][j] for k in range(j)]])
        # print(i, j, h or v)
        # visible += h or v

# print(visible)
print(max(scores))
