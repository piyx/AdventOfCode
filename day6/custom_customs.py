with open('input.txt') as f:
    data = [line.split('\n') for line in f.read().split('\n\n')]


def part1(data):
    total = 0
    for group in data:
        answers = set()
        for person in group:
            answers |= (set(person))  # union

        total += len(answers)

    return total


def part2(data):
    total = 0
    for group in data:
        common_anwers = set(group[0])
        for person in group:
            common_anwers &= set(person)  # intersection

        total += len(common_anwers)

    return total


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
