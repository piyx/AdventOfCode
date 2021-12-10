from collections import defaultdict
import re

Point = tuple[int, int]
Line = tuple[int, int, int, int]

with open("inputs/day5.txt") as f:
    lines = [tuple(map(int, re.findall("\d+", line))) for line in f.readlines()]


def isdiagonal(line: Line) -> bool:
    x1, y1, x2, y2 = line
    return x1 != x2 and y1 != y2

def slope_change(line: Line) -> tuple[int, int]:
    x1, y1, x2, y2 = line
    dx, dy = (-1)**(x1 > x2), (-1)**(y1 > y2)
    if x1 == x2: return 0, dy
    elif y1 == y2: return dx, 0
    else: return dx, dy

def numoverlaps(lines: list[Line], graph: dict[Point, int]) -> int:
    for x1, y1, x2, y2 in lines:
        dx, dy = slope_change((x1, y1, x2, y2))
        while (x1, y1) != (x2, y2):
            graph[x1, y1] += 1
            x1, y1 = x1+dx, y1+dy
        graph[x1, y1] +=1
    
    return sum(overlap > 1 for overlap in graph.values())


if __name__=="__main__":
    graph = defaultdict(int)
    nondiagonals = [line for line in lines if not isdiagonal(line)]
    diagonals = [line for line in lines if isdiagonal(line)]
    print(numoverlaps(nondiagonals, graph))
    print(numoverlaps(diagonals, graph))