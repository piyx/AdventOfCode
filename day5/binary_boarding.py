data = []

# reading the input
with open('input.txt', 'r') as f:
    for line in f:
        data.append(line.strip('\n'))


def part1(data):
    d = []
    low, high, total = float("inf"), 0, 0
    for seat in data:
        row = seat[:-3].translate(str.maketrans({'F': '0', 'B': '1'}))
        col = seat[-3:].translate(str.maketrans({'L': '0', 'R': '1'}))
        num = int(row, 2) * 8 + int(col, 2)
        low = min(low, num)
        high = max(high, num)
        total = total + num

    return low, high, total


def part2(low, high, total):
    return (high*(high+1)//2 - low*(low+1)//2) - total


if __name__ == "__main__":
    low, high, total = part1(data)
    missing = part2(low-1, high, total)
    print(high, missing)
