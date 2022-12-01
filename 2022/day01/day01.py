data = open("./input.txt").read().split("\n\n")

# part 1
cal = [sum(map(lambda x: int(x), di.split())) for di in data]
print(max(cal))

# part 2
print(sum(sorted(cal)[-3:]))
