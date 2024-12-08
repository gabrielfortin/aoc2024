from pprint import pprint
with open("data/data.txt", "r") as f:
    raw = f.readlines()
raw = [i.strip() for i in raw]
matrix = [[j for j in i] for i in raw]
pprint(matrix)

antennas_ij = {}
antennas_types = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        elem = matrix[i][j]
        pos_str = f"{i},{j}"
        if elem != ".":
            antennas_ij[pos_str] = elem
            if elem in antennas_types:
                antennas_types[elem].append((i,j))
            else:
                antennas_types[elem] = [(i,j)]
pprint(antennas_ij)
pprint(antennas_types)

def calc_harmonies(pos1, pos2):
    delta_x = int(pos1[0]) - int(pos2[0])
    delta_y = int(pos1[1]) - int(pos2[1])
    return [(pos1[0]+delta_x, pos1[1]+delta_y),
            (pos2[0]-delta_x, pos2[1]-delta_y)]

from copy import deepcopy
new_mat = deepcopy(matrix)

for antenna_type, positions in antennas_types.items():
    for position1 in positions:
        for position2 in positions:
            if position1 != position2:
                hs = calc_harmonies(position1, position2)
                for h in hs:
                    print(f"h : {h}")
                    if h[0] > -1 and h[1] > -1 and h[0] < len(matrix) and h[1] < len(matrix):
                        new_mat[h[0]][h[1]] = "#"

pprint(new_mat)

count = 0
for i in range(len(new_mat)):
    for j in range(len(new_mat[i])):
        if new_mat[i][j] == "#":
            count += 1
print(count)