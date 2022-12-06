data = open("input.txt").read().strip()

n = 4  # 14 for part 2
for idx in range(len(data[:-4])):
    if len(set(data[idx : idx + n])) == n:
        print(idx + n)
        break
