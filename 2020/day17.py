from collections import Counter
from itertools import product

with open("inputs/input17.txt", "r") as f:
    data = f.read().splitlines()
    cubes1 = {(x, y, 0) for x, r in enumerate(data) for y, c in enumerate(r) if c=='#'}
    cubes2 = {(x, y, 0, 0) for x, r in enumerate(data) for y, c in enumerate(r) if c=='#'}


def cycle(cubes, dimension=3):
    NEIGHBOR = lambda cube, delta: tuple(x + dx for x, dx in zip(cube, delta))
    ADJACENT = set(product([-1, 0, 1], repeat=dimension)) - {(0,) * dimension}
    
    for i in range(6):
        neighbors = Counter(NEIGHBOR(cube, delta) for cube in cubes for delta in ADJACENT)
        cubes = {k for k, v in neighbors.items() if v == 3 or (k in cubes and v == 2)}

    return len(cubes)


if __name__ == "__main__":
    print(cycle(cubes1, dimension=3))
    print(cycle(cubes2, dimension=4))