from itertools import count, product
from copy import deepcopy

with open("inputs/day25.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    H, W = len(grid), len(grid[0])
    east_moving, south_moving, empty = '>', 'v', '.'


def move(grid, sea_cucumber):
    next_spot = lambda i, j: ((i+1) % H, j) if sea_cucumber == south_moving else (i, (j+1) % W)
    new = deepcopy(grid)
    for i, j in product(range(H), range(W)):
        if grid[i][j] != sea_cucumber: continue
        di, dj = next_spot(i, j)
        if grid[di][dj] == empty:
            new[di][dj] = sea_cucumber
            new[i][j] = empty
    
    return new   


prev = grid
for i in count(1):
    prev = grid
    grid = move(grid, sea_cucumber=east_moving)
    grid = move(grid, sea_cucumber=south_moving)
    if prev == grid:
        print(i)
        break