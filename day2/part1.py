with open("data.txt", "r") as f:
    raw = f.readlines()

reports = [[int(i) for i in j.split(" ")] for j in raw]
print(reports)

def all_increasing(levels):
    levels_copy = levels.copy()
    levels_copy.sort()
    return levels_copy == levels

def all_decreasing(levels):
    levels_copy = levels.copy()
    levels_copy.sort()
    levels_copy.reverse()
    return levels_copy == levels

def report_is_safe(levels):
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])

        if diff < 1 or diff > 3:
            return False
    return True

count = 0
for report in reports:
    if (all_increasing(report) or all_decreasing(report)) and report_is_safe(report):
        count += 1
print(count)