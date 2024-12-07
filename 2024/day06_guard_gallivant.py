with open("inputs/day06.txt") as f:
    GRID = [list(line.strip()) for line in f.readlines()]
    START = next((r, c) for r, row in enumerate(GRID) for c, char in enumerate(row) if char == '^')


def move(grid: list[list[str]], start: tuple[int, int]) -> tuple[bool, set]:
    r, c = start
    dr, dc = -1, 0
    visited = {(r, c)}
    seen = {(r, c, dr, dc)}

    while 0 <= (nextr:= r+dr) < len(grid) and 0 <= (nextc:= c+dc) < len(grid[0]):
        if (nextr, nextc, dr, dc) in seen: return True, visited        
        seen.add((nextr, nextc, dr, dc))

        if GRID[nextr][nextc] == '#': 
            dr, dc = dc, -dr
        else: 
            visited.add((nextr, nextc))
            r, c = nextr, nextc

    
    return False, visited
    

def part1() -> int:
    _, visited = move(GRID, START)
    return len(visited)


def part2() -> int:
    _, visited = move(GRID, START)
    visited.remove(START)

    loops = 0

    for r, c in visited:
        GRID[r][c] = '#'
        isloop, _ = move(GRID, START)
        if isloop: loops += 1
        GRID[r][c] = '.'

    return loops


if __name__=="__main__":
    print(part1())
    print(part2())