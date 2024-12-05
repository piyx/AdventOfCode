import itertools
import collections


with open("inputs/day04.txt") as f:
    grid = collections.defaultdict(str) | {
        (r, c): char 
        for r, line in enumerate(f.readlines())
        for c, char in enumerate(line)
    }

    coords = list(grid.keys())


def part1() -> int:
    TARGET = "XMAS"
    DELTAS = [1, 0, -1]

    return sum(
        all(grid[r+i*dr, c+i*dc] == char for i, char in enumerate(TARGET))
        for r, c in coords
        for dr, dc in itertools.product(DELTAS, repeat=2)
    )


def part2() -> int:
    TARGET = ["MAS", "SAM"]
    DELTAS = [1, 0, -1]

    return sum(
        ''.join(grid[r+d, c+d] for d in DELTAS) in TARGET and
        ''.join(grid[r+d, c-d] for d in DELTAS) in TARGET
        for r, c in coords
    )


if __name__=="__main__":
    print(part1())
    print(part2())