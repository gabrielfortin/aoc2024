with open("data.txt", "r") as f:
    data = f.readlines()

left = [int(entry.strip().split(" ")[0]) for entry in data]
right = [int(entry.strip().split(" ")[-1]) for entry in data]

print(left)
print(right)

distances = []

left.sort()
right.sort()

for i in range(len(left)):
    distances.append(abs(left[i]-right[i]))

print(sum(distances))