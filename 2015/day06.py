import re
from itertools import product
from collections import defaultdict

with open('inputs/6', 'r') as f:
    pattern = r'(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)'
    instructions = [[cmd] + list(map(int, coords)) 
                    for line in f.read().splitlines()
                    for cmd, *coords in re.findall(pattern, line)]


def apply(instuctions, todo):
    lights = defaultdict(int)
    
    for cmd, p, q, x, y in instructions:
        for i, j in product(range(p, x+1), range(q, y+1)):
            lights[i, j] = todo[cmd](lights[i, j])
    
    return sum(lights.values())


if __name__ == "__main__":
    todo1 = {'on': lambda x: 1, 'off': lambda x: 0, 'toggle': lambda x: x^1}
    todo2 = {'on': lambda x: x+1, 'off': lambda x: max(0, x-1), 'toggle': lambda x: x+2}
    print(apply(instructions, todo1))
    print(apply(instructions, todo2))
