import itertools


with open("inputs/day02.txt") as f:
    reports = [list(map(int, line.split())) for line in f.readlines()]

LIMIT = 3


def is_strictly_increasing(report: list[int]) -> bool:
    return all(b > a and (b-a) <= LIMIT for a, b in itertools.pairwise(report))


def is_safe(report: list[int]) -> bool:
    return is_strictly_increasing(report) or is_strictly_increasing(report[::-1])


def is_safe_after_dampening(report: list[int]) -> bool:
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))


def part1(reports: list[list[int]]) -> int:
    return sum(is_safe(report) for report in reports)


def part2(reports: list[list[int]]) -> int:
    return sum(is_safe_after_dampening(report) for report in reports)


if __name__=="__main__":
    print(part1(reports))
    print(part2(reports))
