import collections
import math


with open("inputs/day12.txt") as f:
    heightmap = collections.defaultdict(lambda: math.inf)
    
    for row, line in enumerate(f.read().splitlines()):
        for col, height in enumerate(line):
            heightmap[(row, col)] = ord(height)    


def get_positions(heightmap: dict[tuple[int, int], int], height: int) -> list[tuple[int, int]]:
    return [position for position, h in heightmap.items() if h == height]


def shortest_distance(heightmap: dict[tuple[int, int], int], start: tuple[int, int], end: tuple[int, int]) -> int:
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


if __name__=="__main__":
    start = get_positions(heightmap, height=ord('S'))[0]
    end = get_positions(heightmap, height=ord('E'))[0]
    
    heightmap[start], heightmap[end] = ord('a'), ord('z')
    starting_points = get_positions(heightmap, height=ord('a'))

    print(shortest_distance(heightmap, start, end))
    print(min(shortest_distance(heightmap, start, end) for start in starting_points))