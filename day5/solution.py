import functools
import math
with open("data/data.txt", "r") as f:
    raw = f.read()

data1 = raw.split("\n\n")[0]
data2 = raw.split("\n\n")[1]
data2 = [[int(i) for i in entry.split(",")] for entry in data2.split("\n")]

rules = {}
for entry in data1.split("\n"):
    key, value = entry.split("|")
    key = int(key.strip())
    value = int(value.strip())
    if key not in rules:
        rules[key] = [value]
    else:
        rules[key].append(value)

def validate_num(num: str, line):
    valid = True
    if num in rules:
        for rule in rules[num]:
            if rule in line:
                if line.index(rule) < line.index(num):
                    valid = False

    return valid

def compare(a, b):
    if a in rules and b in rules[a]:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def fix_line(line):
    return sorted(line,key=functools.cmp_to_key(compare))

def get_mid(line):
    return line[math.floor(len(line)/2)]

def solve(part: int):
    sum = 0
    for line in data2:
        valid = True
        for num in line:
            if not validate_num(num, line):
                valid = False
        if valid and part == 1:
            sum += get_mid(line)
        elif valid is False and part == 2:
            sum += get_mid(fix_line(line))
    print(sum)

solve(1)
solve(2)