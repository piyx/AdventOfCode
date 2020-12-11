from itertools import product
from pprint import pprint as pp
from copy import deepcopy

with open('inputs/input11.txt', 'r') as f:
    layout = [[seat for seat in row.strip('\n')] for row in f]
    n, m = len(layout), len(layout[0])

adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]


def check_adj(layout, updated, row, col):
    empty = 0
    seat = layout[row][col]
    # print(seat)
    for y, x in adjacent:
        if (0 <= row+y < n) and (0 <= col+x < m):
            # if layout[row+y][col+x] == '#':
            # pass
            # print('lol')
            if layout[row+y][col+x] in 'L.':
                empty += 1
                continue
        else:
            empty += 1
        # print(empty)
    # print(empty, row, col)
    # print(empty, row, col)

    if seat == 'L':
        if empty == 8:
            updated[row][col] = '#'
            return True
        return False
    else:
        if empty <= 4:
            # print('I was here')
            updated[row][col] = 'L'
            return True
        return False


def check_first(layout, updated, row, col):
    empty = 0
    seat = layout[row][col]
    for y, x in adjacent:
        nx, ny = x, y
        while (0 <= row+y < n) and (0 <= col+x < m) and layout[row+y][col+x] not in 'L#':
            y += ny
            x += nx
        if (0 <= row+y < n) and (0 <= col+x < m):
            adj = layout[row+y][col+x]
            if adj == '#':
                continue
            elif adj == 'L':
                empty += 1
            else:
                empty += 1
        else:
            empty += 1
    if seat == 'L':
        if empty == 8:
            updated[row][col] = '#'
            return True
        return False
    else:
        if empty <= 3:
            # print('I was here')
            updated[row][col] = 'L'
            return True
        return False

        # check_adj(layout, 0, 1)
        # print(layout)
        # check_adj(layout, 0, 2)
        # print(layout)
        # check_adj(layout, 0, 3)


def apply_rules1(layout):
    times = 0
    while True:
        changed = False
        updated = deepcopy(layout)
        # print(layout)
        for i in range(n):
            for j in range(m):
                if layout[i][j] == '.':
                    continue
                if check_adj(layout, updated, i, j):
                    # print(i, j)
                    changed = True
        if not changed:
            return updated
            return times
        else:
            times += 1
            # print(times)
        # pp(updated)
        # if times == 3:
            # break
        layout = deepcopy(updated)
        # print(layout)


def apply_rules2(layout):
    times = 0
    while True:
        changed = False
        updated = deepcopy(layout)
        # print(layout)
        for i in range(n):
            for j in range(m):
                if layout[i][j] == '.':
                    continue
                if check_first(layout, updated, i, j):
                    # print(i, j)
                    changed = True
        if not changed:
            return updated
            return times
        else:
            times += 1
            # print(times)
        # pp(updated)
        # if times == 3:
            # break
        layout = deepcopy(updated)
        # print(layout)


final = apply_rules1(layout)
print(sum([s == '#' for row in final for s in row]))

final = apply_rules2(layout)
print(sum([s == '#' for row in final for s in row]))


print(list(product(range(3), range(4))))
