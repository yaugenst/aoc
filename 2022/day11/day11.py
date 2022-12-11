import re
from math import lcm, prod

data = open("input.txt").read().strip().split("\n\n")

m = re.compile(
    r".*?: (?P<items>.*$)\n"
    r".*?= (?P<op>.*$)\n"
    r".*?(?P<test>\d+)\n"
    r".*?(?P<y>\d+)\n"
    r".*?(?P<n>\d+)",
    re.MULTILINE,
)

monkeys = list(map(lambda x: re.search(m, x).groupdict(), data))
for monkey in monkeys:
    monkey["inspect"] = 0
    monkey["items"] = list(map(int, monkey["items"].split(", ")))
    for k, v in monkey.items():
        if type(v) is str and v.isdigit():
            monkey[k] = int(v)

d = lcm(*[x["test"] for x in monkeys])  # for part 2

for _ in range(10000):  # 20 for part 1
    for m in monkeys:
        while m["items"]:
            m["inspect"] += 1
            old = m["items"].pop()
            # new = eval(m["op"]) // 3  # part 1
            new = eval(m["op"]) % d  # part 2
            target = m["y"] if new % m["test"] == 0 else m["n"]
            monkeys[target]["items"].append(new)

print(prod(x["inspect"] for x in sorted(monkeys, key=lambda x: x["inspect"])[-2:]))
