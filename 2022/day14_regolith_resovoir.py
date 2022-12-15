import numpy as np


with open("inputs/day14.txt") as f:
    coords = [
        [tuple(map(int, coord.split(','))) 
         for coord in line.split('->')]
        for line in f.read().splitlines()
    ]

    xmax = max(x for line in coords for x, _ in line)
    ymax = max(y for line in coords for _, y in line)
    cave = np.zeros((ymax+2, xmax+2))
    start = (0, 500)

    for line in coords:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            cave[y1:y2+1, x1:x2+1] = 1    


def drop_sand(x: int, y: int) -> tuple[int, int]: 
    while True:
        if cave[y-1, x] == 0: y += 1
        elif cave[y-1, x-1] == 0: y, x = y-1, x-1
        elif cave[y-1, x+1] == 0: y, x = y-1, x+1
        else: break

        cave[y, x] = 1

def part1(coords: list[list[tuple[int, int]]]) -> int:
    units_dropped += 1

    while True:

        