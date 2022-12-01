#!/usr/bin/env python3

import re
from collections import defaultdict

all_ingredients = []
candidates = defaultdict(set)
for line in open("input.txt"):
    ingredients, allergens = line.split(" (contains ")
    ingredients = ingredients.split()
    all_ingredients += ingredients
    for allergen in re.findall(r"\w+", allergens):
        if allergen in candidates:
            candidates[allergen] &= set(ingredients)
        else:
            candidates[allergen] |= set(ingredients)
safe = set.union(*candidates.values()) ^ set(all_ingredients)
print(sum([all_ingredients.count(ingredient) for ingredient in safe]))

while sum([len(v) for v in candidates.values()]) > len(candidates.keys()):
    for known in (next(iter(v)) for v in candidates.values() if len(v) == 1):
        for unknown in (v for v in candidates.values() if len(v) > 1 and known in v):
            unknown.remove(known)
print(",".join([next(iter(v)) for v in dict(sorted(candidates.items())).values()]))
