data = open("input.txt").read().strip().split()

# part 1
p = 0
for line in data:
    s = len(line) // 2
    a, b = line[:s], line[s:]
    unique = (set(a) & set(b)).pop()
    if unique.islower():
        p += ord(unique) - ord("a") + 1
    else:
        p += ord(unique) - ord("A") + 27
print(p)

# part 2
p = 0
for a, b, c in zip(data[::3], data[1::3], data[2::3]):
    badge = (set(a) & set(b) & set(c)).pop()
    if badge.islower():
        p += ord(badge) - ord("a") + 1
    else:
        p += ord(badge) - ord("A") + 27
print(p)
