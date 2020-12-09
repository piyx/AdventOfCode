def convert(seat):
    row = seat[:-3].translate(str.maketrans({'F': '0', 'B': '1'}))
    col = seat[-3:].translate(str.maketrans({'L': '0', 'R': '1'}))
    return row, col


with open('inputs/input5.txt', 'r') as f:
    data = [convert(line.strip('\n')) for line in f]


def part1(seats):
    low, high, total = float("inf"), 0, 0
    seats = [int(row, 2) * 8 + int(col, 2) for row, col in data]
    for seat in seats:
        low = min(low, seat)
        high = max(high, seat)
        total = total + seat

    return low, high, total


def part2(low, high, total):
    return (high*(high+1)//2 - low*(low+1)//2) - total


if __name__ == "__main__":
    low, high, total = part1(data)
    missing = part2(low-1, high, total)
    print(high, missing)
