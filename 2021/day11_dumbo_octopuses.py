from itertools import product
from itertools import count

with open("inputs/day11.txt") as f:
    octopuses = [list(map(int, line.strip())) for line in f]
    height, width = len(octopuses), len(octopuses[0])
    NEIBORS = lambda y, x: product([y-1, y, y+1], [x-1, x, x+1])
    INBOUND = lambda y, x: 0 <= y < height and 0 <= x < width
    LOOP = list(product(range(height), range(width)))


def flash(y, x):
    global flashes
    flashes += 1
    octopuses[y][x] = -1
    for dy, dx in NEIBORS(y, x):
        if not INBOUND(dy, dx) or octopuses[dy][dx] == -1: continue 
        octopuses[dy][dx] += 1
        if octopuses[dy][dx] >= 10: flash(dy, dx)


flashes = 0
for step in count(1):
    for y, x in LOOP:
        octopuses[y][x] += 1
    
    for y, x in LOOP:
        if octopuses[y][x] >= 10:
            flash(y, x)

    for y, x in LOOP:
        if octopuses[y][x] == -1:
            octopuses[y][x] = 0
    
    if step == 100:
        print(flashes)
    
    if sum(sum(row) for row in octopuses) == 0:
        print(step)
        break