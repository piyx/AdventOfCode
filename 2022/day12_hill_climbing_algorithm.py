import collections
import math

with open("inputs/day12.txt") as f:
    heightmap = collections.defaultdict(lambda: math.inf)
    
    for row, line in enumerate(f.read().splitlines()):
        for col, height in enumerate(line):
            heightmap[(row, col)] = ord(height)

    start = next(position for position, height in heightmap.items() if height == ord('S'))
    end = next(position for position, height in heightmap.items() if height == ord('E'))
    starts = [position for position, height in heightmap.items() if height == ord('a')]
    heightmap[start], heightmap[end] = ord('a'), ord('z')
    starts.append(start)


def shortest_distance(heightmap: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    visited = {start}
    queue = collections.deque([(*start, 0)])

    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == end: return steps

        for dr, dc in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]:
            if heightmap[dr, dc] - heightmap[row, col] > 1: continue
            if (dr, dc) in visited: continue
            
            visited.add((dr, dc))
            queue.append((dr, dc, steps+1))        
    
    return math.inf


def part1(heightmap: dict[tuple[int, int], int], start: tuple[int, int], end: tuple[int, int]) -> int:
    return shortest_distance(heightmap, start, end)


def part2(heightmap: dict[tuple[int, int], int], starts: list[tuple[int, int]], end: tuple[int, int]) -> int:
    return min(shortest_distance(heightmap, start, end) for start in starts)


if __name__=="__main__":
    print(part1(heightmap, start, end))
    print(part2(heightmap, starts, end))