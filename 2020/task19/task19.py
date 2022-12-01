#!/usr/bin/env python3

fp = "input.txt"
rules, msgs = [c.splitlines() for c in open(fp).read().split("\n\n")]
rules = {
    idx: [ri.split() for ri in r.split(" | ")]
    for idx, r in [rule.split(": ") for rule in rules]
}


def remaining(rules, msg, idx):
    for rule in rules[idx]:
        if not rule[0].isdigit():
            if msg and msg[0] == rule[0][1]:
                yield msg[1:]
            continue
        rm = [msg]
        for ri in rule:
            rm = [rms for rmi in rm for rms in remaining(rules, rmi, ri)]
        yield from rm


print(sum("" in remaining(rules, msg, "0") for msg in msgs))
rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]
print(sum("" in remaining(rules, msg, "0") for msg in msgs))
