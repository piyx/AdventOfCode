from collections import defaultdict
from itertools import product

with open("inputs/input17.txt", "r") as f:
    cubes1, cubes2 = set(), set()
    for x, line in enumerate(f.read().splitlines()):
        for y, cube in enumerate(line):
            if cube == "#":
                cubes1.add((x, y, 0))
                cubes2.add((x, y, 0, 0))

NEIGHBOR = lambda cube, delta: tuple(x + dx for x, dx in zip(cube, delta))
ADJACENT = lambda dimension: set(product([-1, 0, 1], repeat=dimension)) - {(0,) * dimension}


def cycle(cubes, dimension=3):
    for i in range(6):
        new_cubes = set(cubes)
        new_candidates = defaultdict(int)
        
        for cube in cubes:
            num = 0
            for delta in ADJACENT(dimension):
                neighbor = NEIGHBOR(cube, delta)
                if neighbor in cubes: num += 1
                else: new_candidates[neighbor] += 1
            
            if num not in [2, 3]: new_cubes.discard(cube)
        
        new_cubes |= {cube for cube, count in new_candidates.items() if count == 3}
        cubes = new_cubes
    
    return len(cubes)

if __name__ == "__main__":
    print(cycle(cubes1, dimension=3))
    print(cycle(cubes2, dimension=4))