import itertools
import dataclasses
import math


@dataclasses.dataclass
class Point:
    x: int
    y: int
    z: int

    def dist(self: Point, other: Point) -> int:
        return (other.x-self.x)**2 + (other.y-self.y)**2 + (other.z-self.z)**2
    
    def __hash__(self):
        return (self.x, self.y, self.z).__hash__()


with open("input.txt") as f:
    points = [Point(*map(int, line.split(","))) for line in f.readlines()]
    pairs = sorted(itertools.combinations(points, r=2), key=lambda x: x[0].dist(x[1]))


def connect(circuits: list[set[Point]], p1: Point, p2: Point):
    matches = [c for c in circuits if p1 in c or p2 in c]
    combined = set().union(*matches).union({p1, p2})
    circuits.append(combined)
    for c in matches: c.clear()
    return [c for c in circuits if c]


def part1():
    circuits = [{point} for point in points]

    for p1, p2 in pairs[:1000]:
        circuits = connect(circuits, p1, p2)

    return math.prod(len(circuit) for circuit in sorted(circuits, key=len, reverse=True)[:3])


def part2():
    circuits = [{point} for point in points]

    for p1, p2 in pairs:
        circuits = connect(circuits, p1, p2)
        if len(circuits) == 1: return p1.x * p2.x


if __name__=="__main__":
    print(part1())
    print(part2())
