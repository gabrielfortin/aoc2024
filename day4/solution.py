from typing import Optional

with open(f"data/test.txt", "r") as f:
    raw = f.readlines()

matrix = [i.strip() for i in raw]

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def print_matrix():
    for i in range(MAT_WIDTH):
        row = ""
        for j in range(MAT_HEIGHT):
            
            if (i,j) in to_print:
                row += f"{getattr(bcolors, to_print[(i,j)])}{matrix[i][j]}{bcolors.ENDC}"
            else:
                row += f"{matrix[i][j]}"
        print(row)

#################### PART 1 ############################
WORD = "XMAS"
MAT_HEIGHT = len(matrix)
MAT_WIDTH = len(matrix[0])

found_indexes = []
to_print = {}
found_words = []

def get_dict(i: int, j: int) -> dict:
    return  {
              "left": (i-1,j),
              "right": (i+1, j),
    
              "up": (i,j+1), 
              "down":(i,j-1), 

              "down-left": (i-1,j-1), 
              "down-right":(i-1,j+1),

              "up-left":(i+1,j-1), 
              "up-right":(i+1, j+1)
    }

def next_char(char: str) -> str:
    next_char = None
    if char != "S":
        index = WORD.index(char)
        next_char = WORD[index+1]
    return next_char

def look_direction(i: int, j: int, char: str, direction: str) -> Optional[bool]:
    global found_indexes
    global to_print

    n_char = next_char(char)
    if n_char is None:
        return
    mat = get_dict(i,j)
    near_item_ij = mat[direction]
 
    try:
        if near_item_ij[0] == -1 or near_item_ij[1] == -1:
            return
        near_item = matrix[near_item_ij[0]][near_item_ij[1]]
    except IndexError:
        return

    print([near_item, n_char])

    if near_item == n_char:
        if n_char == "S":
            found = f"{near_item_ij}{direction}"
            to_print[near_item_ij] = "RED"
            if found not in found_indexes:
                found_indexes.append(found)
            return True
        else:
            r = look_direction(near_item_ij[0], near_item_ij[1], n_char, direction)
            if r is True:
                to_print[near_item_ij] = "GREEN"
                return True


def look_around(i: int, j: int, char: str) -> bool:
    around = get_dict(i,j)
    ret_value = False
              
    for direction, loc in around.items():
        if loc[0] >= 0 and loc[1] >= 0 and \
                loc[0] < MAT_HEIGHT and loc[1] < MAT_WIDTH and \
                matrix[loc[0]][loc[1]] == "M":
            r = look_direction(loc[0], loc[1], char, direction)
            if r is True:
                ret_value = True
                to_print[loc] = "YELLOW"
            
    return ret_value
    
def part1():
    global to_print
    to_print = {}
    for i in range(MAT_WIDTH):
        for j in range(MAT_HEIGHT):
            cur_char = matrix[i][j]
            if cur_char == "X":
                if look_around(i, j, "M"):
                    to_print[(i,j)] = "RED"

    print_matrix()
    print(len([c for c in found_indexes]))


#################### PART 2 ############################
xmas_couples = []

def bound_check(i1: int, j1: int, i2: int, j2: int) -> bool:
    return i1 >= 0 and j1 >= 0 and i1 < MAT_WIDTH and j1 < MAT_HEIGHT and i2>=  0 and j2 >= 0 and i2 < MAT_WIDTH and j2 < MAT_HEIGHT

def check_x(a,b,c,d, char1, char2):
    validation = bound_check(a,b,c,d) and matrix[a][b] == char1 and matrix[c][d] == char2
    if validation:
        global xmas_couples
        to_print[(a,b)] = "RED"
        to_print[(c,d)] = "RED"
    return validation

def part2():
    global to_print
    to_print = {}
    count = 0
    for i in range(MAT_WIDTH):
        for j in range(MAT_HEIGHT):
            cur_char = matrix[i][j]
            if cur_char == "A":
                a=i+1
                b=j+1
                c=i-1
                d=j-1

                if (check_x(a,b,c,d,"M","S") or check_x(a,b,c,d,"S","M")) and \
                    (check_x(a,d,c,b,"M","S") or check_x(a,d,c,b,"S","M")):
                    to_print[(i,j)] = "RED"
                    count += 1
    print_matrix()
    print(count)



part1()
part2()