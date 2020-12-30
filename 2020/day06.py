with open('inputs/input6.txt') as f:
    data = [line.split('\n') for line in f.read().split('\n\n')]


def part1(data):
    return sum(len(set.union(*map(set, group))) for group in data)


def part2(data):
    return sum(len(set.intersection(*map(set, group))) for group in data)


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
