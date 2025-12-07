import functools


with open("input.txt") as f:
    MAP = [line.strip() for line in f.readlines()]
    ROWS, COLS = len(MAP), len(MAP[0])
    STARTROW, STARTCOL = next((row, col) for row, line in enumerate(MAP) for col, item in enumerate(line) if item == 'S')


def splits(row, col, visited=set()):
    if (row, col) in visited: return 0
    if not 0 <= col < COLS: return 0
    if row == ROWS-1: return 0
    visited.add((row, col))
    if MAP[row][col] == '^': return 1 + splits(row, col-1, visited) + splits(row, col+1, visited)
    return splits(row+1, col, visited)


@functools.cache
def timelines(row, col):
    if not 0 <= col < COLS: return 0
    if row == ROWS-1: return 1
    if MAP[row][col] == '^': return timelines(row, col-1) + timelines(row, col+1)
    return timelines(row+1, col)


def part1():
    return splits(STARTROW, STARTCOL)


def part2():
    return timelines(STARTROW, STARTCOL)


if __name__=="__main__":
    print(part1())
    print(part2())
