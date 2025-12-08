import itertools
import math


with open("input.txt") as f:
    points = [tuple(map(int, line.split(","))) for line in f.readlines()]


def dist(point1: tuple[int, int, int], point2: tuple[int, int, int]) -> int:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2


def connect(circuits, p1, p2):
    matches = [c for c in circuits if p1 in c or p2 in c]
    combined = set().union(*matches).union({p1, p2})
    circuits.append(combined)
    for c in matches: c.clear()
    return [c for c in circuits if c]


def part1():
    ordering = sorted(itertools.combinations(points, r=2), key=lambda p: dist(*p))
    circuits = [{point} for point in points]

    for i, (p1, p2) in enumerate(ordering):
        if i == 1000: break
        circuits = connect(circuits, p1, p2)

    lengths = [len(circuit) for circuit in sorted(circuits, key=len, reverse=True)]
    return math.prod(lengths[:3])


def part2():
    ordering = sorted(itertools.combinations(points, r=2), key=lambda p: dist(*p))
    circuits = [{point} for point in points]

    for p1, p2 in ordering:
        circuits = connect(circuits, p1, p2)
        if len(circuits) == 1: return p1[0] * p2[0]


if __name__=="__main__":
    print(part1())
    print(part2())
