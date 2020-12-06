from math import prod

geomap = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# reading the input
with open('inputs/input3.txt', 'r') as f:
    geomap = [line.strip('\n') for line in f]


def part1(geomap, right, down):
    return sum(row[(right*i) % len(row)] == "#" for i, row in enumerate(geomap[::down]))


def part2(geomap, slopes):
    return prod(part1(geomap, right, down) for right, down in slopes)


if __name__ == "__main__":
    print(part1(geomap, 3, 1))
    print(part2(geomap, slopes))
