from copy import deepcopy
from pprint import pprint
with open("data/data.txt", "r") as f:
    raw = f.readlines()
raw = [i.strip() for i in raw]
matrix = [[j for j in i] for i in raw]
#pprint(matrix)

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

def calc_harmonies(pos1, pos2, p1=True):
    delta_x = int(pos1[0]) - int(pos2[0])
    delta_y = int(pos1[1]) - int(pos2[1])

    if p1:
        return [(pos1[0]+delta_x, pos1[1]+delta_y),
                (pos2[0]-delta_x, pos2[1]-delta_y)]
    else:
        hs = []
        base_posx1 = pos1[0]
        base_posy1 = pos1[1]
        base_posx2 = pos2[0]
        base_posy2 = pos2[1]
        for i in range(500):
            hs.append((base_posx1+delta_x, base_posy1+delta_y))
            hs.append((base_posx2-delta_x, base_posy2-delta_y))
            base_posx1+=delta_x
            base_posy1+=delta_y
            base_posx2-=delta_x
            base_posy2-=delta_y
        return hs

def calc(p1=True):
    new_mat = deepcopy(matrix)
    an_locs=dict()

    for antenna_type, positions in antennas_types.items():
        for position1 in positions:
            for position2 in positions:
                if position1 != position2:
                    hs = calc_harmonies(position1, position2, p1=p1)
                    if len(hs) > 0:
                        an_locs[position1]  = 1
                        an_locs[position2]  = 1
                    for h in hs:
                        if p1:
                            if h[0] > -1 and h[1] > -1 and h[0] < len(matrix) and h[1] < len(matrix):
                                new_mat[h[0]][h[1]] = "#"
                        if h[0] > -1 and h[1] > -1 and h[0] < len(matrix) and h[1] < len(matrix):
                            if new_mat[h[0]][h[1]] not in ["#", "."]:
                                an_locs[(h[0],h[1])] = "1"
                            else:
                                new_mat[h[0]][h[1]] = "#"
                                an_locs[(h[0],h[1])] = 1

    if p1:
        pprint(new_mat)
        count = 0
        for i in range(len(new_mat)):
            for j in range(len(new_mat[i])):
                if new_mat[i][j] == "#":
                    count += 1
    else:
        count = len(an_locs.keys())
    
    print(f"{'Part 1' if p1 else 'Part 2'} answer : {count}")

calc(p1=True)
calc(p1=False)