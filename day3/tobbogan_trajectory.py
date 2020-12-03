from math import prod
geomap = []

# reading the input
with open('input.txt', 'r') as f:
    for line in f:
        geomap.append(list(line.strip('\n')))


def part1(geomap, right, down):
    trees = 0
    for i, row in enumerate(geomap[::down]):
        idx = (right*i) % len(geomap[0])
        if row[idx] == '#':
            trees += 1

    return trees


def part2(geomap):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(part1(geomap, right, down) for right, down in slopes)


if __name__ == "__main__":
    print(part1(geomap, 3, 1))
    print(part2(geomap))
