import itertools


with open("inputs/day08.txt") as f:
    grid = {
        x + y * 1j: char
        for x, line in enumerate(f.readlines())
        for y, char in enumerate(line.strip())
    }


def signal_impact(signal_range: list[int]):
    antennas = set(grid.values()) - {"."}
    antinodes = set()

    for antenna in antennas:
        positions = [position for position, char in grid.items() if char == antenna]
        antinodes |= {
            antinode
            for p1, p2 in itertools.permutations(positions, r=2)
            for i in signal_range
            if (antinode := (p1 - i * (p2 - p1))) in grid
        }

    return len(antinodes)


def part1():
    return signal_impact(signal_range=[1])


def part2():
    totalrows = max(grid, key=lambda x: x.real) + 1
    return signal_impact(signal_range=range(0, totalrows))


if __name__ == "__main__":
    print(part1())
    print(part2())
