#!/usr/bin/env python3

import re

fp = "input.txt"
data = [line for line in open(fp).read().split("\n") if line]


class N1:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        return N1(self.x + y.x)

    def __sub__(self, y):
        return N1(self.x * y.x)


print(sum([eval(re.sub(r"(\d+)", r"N1(\1)", s.replace("*", "-"))).x for s in data]))


class N2:
    def __init__(self, x):
        self.x = x

    def __mul__(self, y):
        return N2(self.x * y.x)

    def __pow__(self, y):
        return N2(self.x + y.x)


print(sum([eval(re.sub(r"(\d+)", r"N2(\1)", s.replace("+", "**"))).x for s in data]))
