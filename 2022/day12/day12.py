data = list(map(list, open("input.txt").read().strip().split()))
grid = {}
start = None
end = None
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            start = (i, j)
            grid[(i, j)] = 0
        elif data[i][j] == "E":
            end = (i, j)
            grid[(i, j)] = 25
        else:
            grid[(i, j)] = ord(data[i][j]) - ord("a")


adjacency = {}
for i, j in grid:
    adjacency[(i, j)] = []
    for y, x in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= x < len(data[0]) and 0 <= y < len(data):
            adjacency[(i, j)].append((y, x))


def bfs(nodes, edges, start, end):
    visited = set()
    queue = [(0, end)]
    while queue:
        steps, pos = queue.pop(0)
        if pos in start:
            return steps
        for edge in edges[pos]:
            if edge not in visited and nodes[pos] - nodes[edge] <= 1:
                visited.add(edge)
                queue.append((steps + 1, edge))
    return -1


print(bfs(grid, adjacency, [start], end))  # part 1
print(bfs(grid, adjacency, [k for k, v in grid.items() if v == 0], end))  # part 2
