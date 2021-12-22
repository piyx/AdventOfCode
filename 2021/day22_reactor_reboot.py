from collections import Counter
from typing import NamedTuple
from math import inf
import re


class Cube(NamedTuple):
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def volume(self):
        return (self.x2-self.x1+1) * (self.y2-self.y1+1) * (self.z2-self.z1+1)

    def intersection(self, other):
        x1, x2 = max(self.x1, other.x1), min(self.x2, other.x2)
        y1, y2 = max(self.y1, other.y1), min(self.y2, other.y2)
        z1, z2 = max(self.z1, other.z1), min(self.z2, other.z2)
        if x1 <= x2 and y1 <= y2 and z1 <= z2:
            return Cube(x1, x2, y1, y2, z1, z2)
        return None
    
    def inbound(self, bounds):
        return all((
            bounds[0] <= self.x1 and self.x2 <= bounds[1],
            bounds[0] <= self.y1 and self.y2 <= bounds[1],
            bounds[0] <= self.z1 and self.z2 <= bounds[1],
        ))


def solve(inputs, bounds):
    cubes = Counter()
    for switch, cube in inputs:  
        if not cube.inbound(bounds): continue

        for oldcube, count in cubes.copy().items():
            overlap = cube.intersection(oldcube)
            if overlap is None: continue
            cubes[overlap] -= count
        
        if switch: cubes[cube] += switch

    return sum(cube.volume()*count for cube, count in cubes.items())


with open("inputs/day22.txt") as f:
    inputs = [
        [switch=="on", Cube(*map(int, re.findall('-?\d+', coords)))]
        for switch, coords in map(str.split, f.readlines())
    ]


print(solve(inputs, bounds=[-50, 50]))
print(solve(inputs, bounds=[-inf, inf]))