with open("data.txt", "r") as f:
    data = f.readlines()

left = [int(entry.strip().split(" ")[0]) for entry in data]
right = [int(entry.strip().split(" ")[-1]) for entry in data]

print(left)
print(right)

scores = []

left.sort()
right.sort()

for i in range(len(left)):
    right.count(left[i])*left[i]
    scores.append(right.count(left[i])*left[i])

print(sum(scores))