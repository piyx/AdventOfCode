import math
import re

with open("inputs/day17.txt") as f:
    x1, x2, y1, y2 = map(int, re.findall(r'([-]*\d+)', f.read()))


def simulate(dx, dy):
    x, y = (0, 0)

    while x <= x2 and y >= min(y1, y2):
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        
        x, y = x+dx, y+dy
        dx = dx-1 if dx > 0 else dx+1 if dx < 0 else 0
        dy -= 1
    
    return False

def part1():
    return y1*(y1+1)//2

def part2():
    minsteps = (-1 + (math.sqrt(1 + 8*x1))) / 2

    return sum(
        simulate(dx, dy)
        for dx in range(int(minsteps), x2+1)
        for dy in range(y1, abs(y1)+1) 
    )


print(part1())
print(part2())