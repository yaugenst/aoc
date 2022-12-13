from functools import cmp_to_key


def compare(a, b):
    match a, b:
        case int(), int():
            if a < b:
                return 1
            elif a == b:
                return 0
            else:
                return -1
        case list(), list():
            for ai, bi in zip(a, b):
                if (x := compare(ai, bi)) != 0:
                    return x
            return compare(len(a), len(b))
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])


data = open("input.txt").read().strip().split("\n\n")
data = [list(map(eval, x.split("\n"))) for x in data]

result = 0
for i, (a, b) in enumerate(data, 1):
    if compare(a, b) == 1:
        result += i
print(result)


div = [[2], [6]]
part2 = sum(data, div)
result = 1
for i, line in enumerate(sorted(part2, key=cmp_to_key(compare), reverse=True), 1):
    if line in div:
        result *= i
print(result)
