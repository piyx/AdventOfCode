import re

# reading the input
with open("inputs/input2.txt", 'r') as f:
    data = [re.split('-| |: ', line.strip('\n')) for line in f]


def part1(data):
    return sum(int(low) <= s.count(char) <= int(high) for low, high, char, s in data)


def part2(data):
    return sum((s[int(low)-1] == char) ^ (s[int(high)-1] == char) for low, high, char, s in data)


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
