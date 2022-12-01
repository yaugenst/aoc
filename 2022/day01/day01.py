data = open("./input.txt").read().split("\n\n")

# part 1
cal = [sum(map(int, di.split())) for di in data]
print(max(cal))

# part 2
print(sum(sorted(cal)[-3:]))
