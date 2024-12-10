class Block:
    def __init__(self, bid: int, value: int, btype: str):
        self._bid = bid
        self._value = value
        self._btype = btype

    def __str__(self):
        if self._btype=="free":
            return "."*self._value
        else:
            return f"{self._bid}"*self._value

FILENAME = "data"
with open(f"data/{FILENAME}.txt", "r") as f:
    raw = f.read()

print(raw)
blocks = list()
files = list()
for i in range(len(raw)):
    btype = "free"
    if i%2 == 0:
        btype = "file"
    blocks.append(Block(bid=int(i/2), value=int(raw[i]), btype=btype))

R = "".join([str(b) for b in blocks])
print(R)
R = [str(c) for c in R]

free_indexes = list()
file_indexes = list()
for i in range(len(R)):
    c = R[i]
    if c == ".":
        free_indexes.append(i)
    else:
        file_indexes.append(i)

for index in free_indexes:
    #print(index)
    #print("".join(R))
    if all([R[i] == "." for i in range(index+1, len(R))]):
        break

    R[index] = str(R[int(file_indexes[-1])])
    
    R[file_indexes[-1]] = "."
    
    file_indexes = file_indexes[:-1]


    
def calc_checksum(R: list):
    checksum = 0
    for i in range(len(R)):
        if R[i] != ".":
            checksum += i*int(R[i])
    return checksum

#print("".join(R))
print(calc_checksum(R))