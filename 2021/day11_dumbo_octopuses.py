from itertools import product
from itertools import count

with open("inputs/day11.txt") as f:
    OCTOPUSES = [list(map(int, line.strip())) for line in f]
    HEIGHT, WIDTH = len(OCTOPUSES), len(OCTOPUSES[0])
    NEIBORS = lambda y, x: product([y-1, y, y+1], [x-1, x, x+1])
    INBOUND = lambda y, x: 0 <= y < HEIGHT and 0 <= x < WIDTH
    LOOP = list(product(range(HEIGHT), range(WIDTH)))


def flash(y, x):
    global flashes
    flashes += 1
    OCTOPUSES[y][x] = -1
    for dy, dx in NEIBORS(y, x):
        if not INBOUND(dy, dx) or OCTOPUSES[dy][dx] == -1: continue 
        OCTOPUSES[dy][dx] += 1
        if OCTOPUSES[dy][dx] >= 10: flash(dy, dx)


flashes = 0
for step in count(1):
    for y, x in LOOP:
        OCTOPUSES[y][x] += 1
    
    for y, x in LOOP:
        if OCTOPUSES[y][x] >= 10:
            flash(y, x)

    for y, x in LOOP:
        if OCTOPUSES[y][x] == -1:
            OCTOPUSES[y][x] = 0
    
    if step == 100:
        print(flashes)
    
    if sum(sum(row) for row in OCTOPUSES) == 0:
        print(step)
        break