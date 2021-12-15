import heapq

with open("inputs/day15.txt") as f:
    cave = [list(map(int, line.strip())) for line in f.readlines()]
    height, width = len(cave), len(cave[0])


def in_cave(y, x, cave_size):
    return 0 <= y < height*cave_size and 0 <= x < width*cave_size

def risk_level(cave, y, x, size=1):
    risk_level = cave[y%height][x%width] + x//height + y//width
    if risk_level >= 10:
        risk_level = risk_level%10 + 1
    
    return risk_level

def dijkstras(cave, cave_size=1):
    src, dest = (0, 0), (height*cave_size-1, width*cave_size-1)
    heap, visited = [(0,) + src], {src}
    while heap:
        risk, y, x = heapq.heappop(heap)
        if (y, x) == dest: return risk

        for dy, dx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
            if (dy, dx) in visited or not in_cave(dy, dx, cave_size):
                continue            
                
            r = risk_level(cave, dy, dx, size=1)
            if r == float('inf'): continue
            heapq.heappush(heap, (risk+r, dy, dx))
            visited.add((dy, dx))


print(dijkstras(cave, cave_size=1))
print(dijkstras(cave, cave_size=5))