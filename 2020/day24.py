from collections import defaultdict
from collections import Counter
import re


DIRECTIONS = {'e': 2, 'w': -2, 'ne': 1-2j, 'nw': -1-2j, 'se': 1+2j, 'sw': -1+2j}
TILES = defaultdict(int)

with open('inputs/input24.txt', 'r') as f:
    data = [re.findall(r'e|w|se|ne|sw|nw', line) for line in f.read().splitlines()]

for line in data: 
    TILES[sum(DIRECTIONS[d] for d in line)] ^= 1

black = set(tile for tile, state in TILES.items() if state)
for _ in range(100):
    neighbors = Counter(tile+dir for tile in black for dir in DIRECTIONS.values())
    black = {k for k, v in neighbors.items() if (k in black and v in [1, 2]) or (k not in black and v==2)}


if __name__ == "__main__":
    print(sum(TILES.values()))
    print(len(black))