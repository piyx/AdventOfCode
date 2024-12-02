from collections import Counter


with open("inputs/day01.txt") as f:
    leftlist = []
    rightlist = []

    for line in f.readlines():
        left, right = map(int, line.split())
        leftlist.append(left)
        rightlist.append(right)


def part1(leftlist: list[int], rightlist: list[int]) -> int:
    return sum(abs(left-right) for left, right in zip(sorted(leftlist), sorted(rightlist)))


def part2(leftlist: list[int], rightlist: list[int]) -> int:
    leftcounts = Counter(leftlist)
    rightcounts = Counter(rightlist)
    return sum(num * leftcounts[num] * rightcounts[num] for num in leftcounts)


if __name__=="__main__":
    print(part1(leftlist, rightlist))
    print(part2(leftlist, rightlist))