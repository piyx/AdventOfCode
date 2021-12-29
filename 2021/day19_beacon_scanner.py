from collections import defaultdict
from itertools import permutations
from itertools import product
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
    z: int

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


def generate_orientations(scanner):
    for p in permutations([0, 1, 2]):
        for r in product([-1, 1], repeat=3):
            yield [Point(*[beacon[i] * r[i] for i in p]) for beacon in scanner]


def locate_scanner(i, j):
    for scanner_orientaion in generate_orientations(scanners[j]):
        overlaps = defaultdict(int)
        for beacon1 in scanners[i]:
            for beacon2 in scanner_orientaion:
                overlaps[beacon1 - beacon2] += 1

        for scanner_position, overlap in overlaps.items():
            if overlap < 12:
                continue

            scanners[j] = [beacon + scanner_position for beacon in scanner_orientaion]
            located_scanners.append(j)
            unlocated_scanners.remove(j)
            scanner_positions[j] = scanner_position
            return


with open("inputs/day19.txt") as f:
    scanners = [
        [Point(*map(int, line.split(","))) for line in chunk.split("\n")[1:]]
        for chunk in f.read().split("\n\n")
    ]

    located_scanners = [0]
    unlocated_scanners = set(range(1, len(scanners)))
    scanner_positions = [Point(0, 0, 0)] * len(scanners)


def part1():
    while located_scanners:
        i = located_scanners.pop()
        for j in unlocated_scanners.copy():
            locate_scanner(i, j)

    return len(set.union(*map(set, scanners)))


def part2():
    return max(
        scanner1.manhattan_distance(scanner2)
        for scanner1 in scanner_positions
        for scanner2 in scanner_positions
    )


print(part1())
print(part2())
