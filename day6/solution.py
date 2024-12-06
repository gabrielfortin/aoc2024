from typing import Optional

CURSORS = {
    ">": (1,0), 
    "<": (-1,0), 
    "^": (0,-1), 
    "v": (0,1)
}

CURSORS_ORDER = [">", "v", "<", "^"]

class LutinDeMerde:
    def __init__(self, filename: str = None, matrix: list = None):
        if filename is not None:
            with open(f"data/{filename}.txt", "r") as f:
                raw = f.readlines()
            self._matrix = [[j for j in i.strip()] for i in raw]
        elif matrix is not None:
            self._matrix = matrix
        self._current_x = 0
        self._current_y = 0
        self._current_dir = "^"
        self.locate_cursor()
        self._visited = dict()
        self.add_to_visited()

    def locate_cursor(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j] in CURSORS:
                    self._current_x = i
                    self._current_y = j
                    self._current_dir = self._matrix[i][j]
                    return
                
    def walk(self, print_info=True):
        """
        Walk through the matrix until the cursor goes out of bounds
        """
        iterations = 0
        while True:
            res = self.step()
            iterations +=1

            if iterations > 10000:
                print("loop detected")
                return "loop"

            if res is True:
                if print_info:
                    self.print_map()
                    print(self._current_x, self._current_y, self._current_dir)
                    print(f"{iterations} iterations")
                    print(f"Total visited : {len(self._visited)}")
                break

    def step(self) -> Optional[bool]:
        """
        Move the cursor to the next cell (1 iteration)
        """
        new_x = self._current_x + CURSORS[self._current_dir][1]
        new_y = self._current_y + CURSORS[self._current_dir][0]

        if new_x < 0 or new_x >= len(self._matrix) or new_y < 0 or new_y >= len(self._matrix[0]):
            return True
        elif self._matrix[new_x][new_y] == ".":
            #print(new_x, new_y)
            self._matrix[self._current_x][self._current_y] = "."
            self._current_x = new_x
            self._current_y = new_y
            self.add_to_visited()
        elif self._matrix[new_x][new_y] in ["#", "O"]:
            self.turn()
        else:
            print("error")
            print(self._matrix[new_x][new_y])
            return
    
    def turn(self):
        """
        Change the direction of the cursor
        """
        i = CURSORS_ORDER.index(self._current_dir)
        if i+1 < len(CURSORS_ORDER):
            self._current_dir = CURSORS_ORDER[i+1]
        else:
            self._current_dir = CURSORS_ORDER[0]
        #print(self._current_dir)

    def add_to_visited(self):
        """
        Add the current position to the visited cells
        """
        index = f"{self._current_x},{self._current_y}"
        if  index in self._visited:
            self._visited[index] += 1
        else:
            self._visited[index] = 0

    def print_map(self):
        """
        Print the map with the cursor and the visited cells
        """
        new_mat = self._matrix.copy()
        for visited in self._visited.keys():
            new_mat[int(visited.split(",")[0])][int(visited.split(",")[1])] = "X"
        new_mat[self._current_x][self._current_y] = self._current_dir
        for i in new_mat:
            print("".join(i))

p1=LutinDeMerde("test")
print(p1._current_x, p1._current_y, p1._current_dir)
p1.walk()

p1=LutinDeMerde("data")
print(p1._current_x, p1._current_y, p1._current_dir)
p1.walk()

## P2
if True:
    with open(f"data/data.txt", "r") as f:
        raw = f.readlines()
        matrix = [[j for j in i.strip()] for i in raw]

    def get_all_dots(matrix):
        indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == ".":
                    indexes.append((i,j))
        return indexes

    dots_ij = get_all_dots(matrix)
    summ = 0
    count = 0
    for index in dots_ij:
        with open(f"data/data.txt", "r") as f:
            raw = f.readlines()
            new_mat = [[j for j in i.strip()] for i in raw]
        new_mat[index[0]][index[1]] = "O"

        lutin = LutinDeMerde(matrix=new_mat)
        if lutin.walk(False) == "loop":
            summ+=1
        count += 1
        print(f"{100*count/len(dots_ij)}%")

    print(summ)