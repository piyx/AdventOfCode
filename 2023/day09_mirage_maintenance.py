import itertools


with open("inputs/day09.txt") as f:
    readings = [list(map(int, line.split())) for line in f.read().splitlines()]


def predict(values: list[int]) -> int:
    rows = [values]
    diff = values

    while set(diff) != {0}:
        diff = [curr-prev for prev, curr in itertools.pairwise(diff)]
        rows.append(diff)

    return sum(diff[-1] for diff in rows)


def part1(readings: list[list[int]]) -> int:
    return sum(predict(values) for values in readings)


def part2(readings: list[list[int]]) -> int:
    return sum(predict(values[::-1]) for values in readings)


print(part1(readings))
print(part2(readings))