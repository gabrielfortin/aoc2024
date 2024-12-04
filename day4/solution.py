with open(f"data/data.txt", "r") as f:
    raw = f.readlines()

matrix = [i.strip() for i in raw]

WORD = "XMAS"
MAT_HEIGHT = len(matrix)
MAT_WIDTH = len(matrix[0])
CURRENT_WORD = ""

found_indexes = []
found_s = []
found_a = []
found_m = []
found_words = []

def get_dict(i,j):
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

def next_char(char):
    next_char = None
    if char != "S":
        index = WORD.index(char)
        next_char = WORD[index+1]
    return next_char

def look_direction(i, j, char, direction):
    global found_indexes
    global found_s
    global found_a
    global CURRENT_WORD

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
            CURRENT_WORD += n_char
            found_words.append(CURRENT_WORD)
            print("found")
            found = f"{near_item_ij}{direction}{CURRENT_WORD}"
            found_s.append(near_item_ij)
            if found not in found_indexes:
                found_indexes.append(found)
            return True
        else:
            CURRENT_WORD += n_char
            r = look_direction(near_item_ij[0], near_item_ij[1], n_char, direction)
            if r is True:
                found_a.append(near_item_ij)
                return True


def look_around(i, j, char):
    global CURRENT_WORD
    global found_m

    around = get_dict(i,j)
              
    for direction, loc in around.items():
        if loc[0] >= 0 and loc[1] >= 0 and \
                loc[0] < MAT_HEIGHT and loc[1] < MAT_WIDTH and \
                matrix[loc[0]][loc[1]] == "M":
            CURRENT_WORD += char
            r = look_direction(loc[0], loc[1], char, direction)
            if r is True:
                found_m.append(loc)
            
    return False

    
def part1():
    global CURRENT_WORD
    for i in range(MAT_WIDTH):
        for j in range(MAT_HEIGHT):
            cur_char = matrix[i][j]
            if cur_char == "X":
                CURRENT_WORD = cur_char
                look_around(i, j, "M")


part1()

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

for i in range(MAT_WIDTH):
    row = ""
    for j in range(MAT_HEIGHT):
        
        if (i,j) in found_s:
            row += f"{bcolors.RED}{matrix[i][j]}{bcolors.ENDC}"
        elif (i,j) in found_a:
            row += f"{bcolors.OKGREEN}{matrix[i][j]}{bcolors.ENDC}"
        elif (i,j) in found_m:
            row += f"{bcolors.WARNING}{matrix[i][j]}{bcolors.ENDC}"
        else:
            row += f"{matrix[i][j]}"
    print(row)

print(len([word for word in found_words if "MAS" in word]))