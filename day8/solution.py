from copy import deepcopy
from pprint import pprint
from typing import Tuple, Optional, List

HARMONIES_CALC_LIMIT = 50

# Parse data
with open("data/data.txt", "r") as f:
    raw = f.readlines()
raw = [i.strip() for i in raw]
matrix = [[j for j in i] for i in raw]

# Identify antennas
antennas_types = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        elem = matrix[i][j]
        pos_str = f"{i},{j}"
        if elem != ".":
            if elem in antennas_types:
                antennas_types[elem].append((i,j))
            else:
                antennas_types[elem] = [(i,j)]

def calc_harmonies(pos1: Tuple[int, int], pos2: Tuple[int, int], p1: Optional[bool]=True) -> List[Tuple[int,int]]:
    """
    calculate harmonies
    :param pos1: position of the first antenna
    :param pos2: position of the first antenna
    :param p1: If true, will calculate for part 1 of day 8, otherwise, for part 2
    """
    delta_x = int(pos1[0]) - int(pos2[0])
    delta_y = int(pos1[1]) - int(pos2[1])

    if p1:
        return [(pos1[0]+delta_x, pos1[1]+delta_y),
                (pos2[0]-delta_x, pos2[1]-delta_y)]
    else:
        hs = []
        p_vector = [pos1[0], pos1[1], pos2[0], pos2[1]]
        d_vector = [delta_x, delta_y, 0-delta_x, 0-delta_y]
        for i in range(HARMONIES_CALC_LIMIT):
            hs.extend([(p_vector[0]+delta_x, p_vector[1]+delta_y), (p_vector[2]-delta_x, p_vector[3]-delta_y)])
            p_vector = [a + b for a, b in zip(p_vector, d_vector)]
        return hs

def calc(p1: Optional[bool] = True):
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