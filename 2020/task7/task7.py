#!/usr/bin/env python3

import re

c_expr = re.compile(r"(\w+ \w+) bag")
n_expr = re.compile(r"(\d+)")
rules = {}
for line in open("input.txt"):
    c = c_expr.findall(line)
    n = n_expr.findall(line)
    rules[c[0]] = {ci: int(ni) for ci, ni in zip(c[1:], n)}

def count_possible(rule, key, rules):
    if key in rule.keys():
        return [1]
    return map(sum, [count_possible(rules[r], key, rules) for r in rule.keys()])

def count_inside(rule, rules):
    if not rule:
        return 0
    n = sum(rule.values())
    return [n] + [v * [count_inside(rules[k],  rules)] for k, v in rule.items()]

mybag = "shiny gold"

res = 0
for k, v in rules.items():
    res += sum(count_possible(v, mybag, rules)) > 0
print(res)

# this is the most ridiculous thing ever, sue me
counts = str(count_inside(rules[mybag], rules)).replace("[", "").replace("]", "").split(", ")
print(sum(int(c) for c in counts))
