with open("inputs/day06.txt") as f:
    GRID = {r+c*1j: char for r, line in enumerate(f.readlines()) for c, char in enumerate(line.strip())}
    START = next(position for position, char in GRID.items() if char == '^')


def move(grid: dict[complex: str], start: complex) -> tuple[bool, set]:
    position = start
    direction = -1
    visited = {position}
    seen = {(position, direction)}

    while (nextpos := position+direction) in grid:
        if (nextpos, direction) in seen: return True, visited        
        seen.add((nextpos, direction))

        if grid[nextpos] == '#': 
            direction *= -1j
        else: 
            visited.add(nextpos)
            position = nextpos


    return False, visited
    

def part1(grid: dict[complex, str], start: complex) -> int:
    visited = move(grid, start)[1]
    return len(visited)


def part2(grid: dict[complex, str], start: complex) -> int:
    visited = move(grid, start)[1]
    visited.remove(start)
    return sum(move(grid | {position: '#'}, start)[0] for position in visited)


if __name__=="__main__":
    print(part1(GRID, START))
    print(part2(GRID, START))