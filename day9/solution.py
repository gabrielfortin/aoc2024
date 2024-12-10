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

FILENAME = "test"
with open(f"data/{FILENAME}.txt", "r") as f:
    raw = f.read()

print(raw)
blocks = list()
for i in range(len(raw)):
    btype = "free"
    if i%2 == 0:
        btype = "file"
    blocks.append(Block(bid=int(i/2), value=int(raw[i]), btype=btype))

print("".join([str(b) for b in blocks]))