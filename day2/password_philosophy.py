data = []

# reading the input
with open("input.txt", 'r') as f:
    for line in f:
        limit, char, string = line.split()
        lower, upper = list(map(int, limit.split('-')))
        data.append((lower, upper, char[:-1], string))


def part1(data):
    ans = 0
    for lower, upper, char, string in data:
        if lower <= string.count(char) <= upper:
            ans += 1
    return ans


def part2(data):
    ans = 0
    for lower, upper, char, string in data:
        left, right = string[lower-1], string[upper-1]
        if left == right == char:
            continue

        if left == char or right == char:
            ans += 1

    return ans


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
