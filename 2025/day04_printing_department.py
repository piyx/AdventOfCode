import itertools


with open("input.txt") as f:
    rolls = {
        (row, col) 
        for row, line in enumerate(f.read().splitlines()) 
        for col, item in enumerate(line.strip())
        if item == '@'
    }

    adjacent = set(itertools.product([-1, 0, 1], repeat=2)) - {(0, 0)}


def accessible_rolls(rolls):
    return {
        (row, col) 
        for row, col in rolls 
        if sum((row+dr, col+dc) in rolls for dr, dc in adjacent) < 4
    }


def part1(rolls: set[tuple[int, int]]) -> int:
    return len(accessible_rolls(rolls))


def part2(rolls: set[tuple[int, int]]) -> int:
    removed = 0

    while True:
        accessible = accessible_rolls(rolls)
        if not accessible: return removed

        removed += len(accessible)
        rolls = rolls - accessible


if __name__=="__main__":
    print(part1(rolls))
    print(part2(rolls))
