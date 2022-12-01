#!/usr/bin/env python3

import re

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
expr = re.compile(r"([^\s]+):([^\s]+)")
passports = [{}]

for line in open("input.txt", "r"):
    if any(entry := expr.findall(line)):
        passports[-1].update({k: v for k, v in entry})
    else:
        if not all([k in passports[-1].keys() for k in req_fields]):
            passports.pop()

        passports.append({})

print(len(passports))

def is_valid(p):
    if not all([p["byr"].isdecimal(), 1920 <= int(p["byr"]) <= 2002]):
        return False
    if not all([p["iyr"].isdecimal(), 2010 <= int(p["iyr"]) <= 2020]):
        return False
    if not all([p["eyr"].isdecimal(), 2020 <= int(p["eyr"]) <= 2030]):
        return False
    if not p["hgt"][-2:] in ["cm", "in"]:
        return False
    if p["hgt"][-2:] == "cm" and not 150 <= int(p["hgt"][:-2]) <= 193:
        return False
    if p["hgt"][-2:] == "in" and not 59 <= int(p["hgt"][:-2]) <= 76:
        return False
    if not all([p["hcl"][0] == "#", len(p["hcl"][1:]) == 6]):
        return False
    if not p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not all([p["pid"].isdecimal(), len(p["pid"]) == 9]):
        return False
    return True

print(len([p for p in passports if is_valid(p)]))
