import re

with open("data.txt", "r") as f:
    raw = f.read()

def process_mul(expr) -> int:
    return eval(expr.replace("mul", "").replace("(", "").replace(")", "").replace(",", "*"))

def part1() -> int:
    expr = "mul+\(+\d+\,+\d+\)"
    operations = re.findall(expr, raw)
    sum = 0
    for oper in operations:
        sum += process_mul(oper)
    return sum

def part2() -> int:
    expr = "((don+\'+t|do)+\(+\))|(mul+\(+\d+\,+\d+\))"
    operations = re.findall(expr, raw)
    sum = 0
    enabled = True
    for oper in operations:
        if oper[0] == "do()":
            enabled = True
        elif oper[0] == "don't()":
            enabled = False
        
        if enabled and re.search("mul+\(+\d+\,+\d+\)", oper[2]):
            sum += process_mul(oper[2])

    return sum

print(part1())
print(part2())