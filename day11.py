from pprint import pprint as pp
from copy import deepcopy
from itertools import product

with open('inputs/input11.txt', 'r') as f:
    layout = [[seat for seat in row.strip('\n')] for row in f]

N, M = len(layout), len(layout[0])

ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]


def inbound(row, col):
    return (0 <= row < N) and (0 <= col < M)


def empty_adjacent(layout, row, col):
    return sum((not inbound(row+y, col+x) or layout[row+y][col+x] in 'L.' for y, x in ADJACENT))


def empty_first(layout, row, col):
    empty = 0
    for y, x in ADJACENT:
        dy, dx = y, x
        while inbound(row+dy, col+dx) and layout[row+dy][col+dx] not in 'L#':
            dy, dx = dy+y, dx+x

        if inbound(row+dy, col+dx) and layout[row+dy][col+dx] == '#':
            continue

        empty += 1

    return empty


def occupied(layout, func, rule):
    while True:
        changed = False
        updated = deepcopy(layout)
        for i, j in product(range(N), range(M)):
            seat = layout[i][j]
            if seat == '.':
                continue
            empty = func(layout, i, j)
            if seat == 'L' and empty == 8 or seat == '#' and empty <= (8-rule):
                changed = True
                updated[i][j] = '#' if updated[i][j] == 'L' else 'L'

        layout = updated

        if not changed:
            break

    return sum(seat == '#' for row in layout for seat in row)


if __name__ == "__main__":
    print(occupied(layout, empty_adjacent, 4))
    print(occupied(layout, empty_first, 5))
