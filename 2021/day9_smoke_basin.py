from itertools import product
import math

with open("inputs/day9.txt") as f:
    cave = [list(map(int, line.strip())) for line in f.readlines()]
    height, width = len(cave), len(cave[0])

inbound = lambda y, x: 0 <= y < height and 0 <= x < width
neibors = lambda y, x: [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]


def part1(cave):
    def risklevel(y, x):
        islowpoint = all(cave[y][x] < cave[dy][dx] for dy, dx in neibors(y, x) if inbound(dy, dx))
        return 1+cave[y][x] if islowpoint else 0
    
    return sum(risklevel(y, x) for y, x in product(range(height), range(width)))


def part2(cave):
    def dfs(y, x):
        if not inbound(y, x) or cave[y][x] == 9: return 0
        cave[y][x] = 9 # Mark as visited
        return 1+sum(dfs(dy, dx) for dy, dx in neibors(y, x))    
    
    basins = [dfs(y, x) for y, x in product(range(height), range(width))]
    return math.prod(sorted(basins, reverse=True)[:3])


print(part1(cave))
print(part2(cave))