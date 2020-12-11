from copy import deepcopy
from itertools import product

with open('inputs/input11.txt', 'r') as f:
    layout = [[seat for seat in row.strip('\n')] for row in f]


ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
N, M = len(layout), len(layout[0])


inbound = lambda row, col: (0 <= row < N) and (0 <= col < M)


def emptyadjacent(layout, row, col):
    '''Return number of empty adjacent seats'''
    return sum((not inbound(row+y, col+x) or layout[row+y][col+x] in 'L.' for y, x in ADJACENT))


def emptyfirst(layout, row, col):
    '''Return the number of empty visible seats'''

    def helper(layout, row, col, dx, dy):
        x, y = dx, dy
        while inbound(row+y, col+x) and layout[row+y][col+x] not in 'L#':
            x, y = x+dx, y+dy
    
        return not(inbound(row+y, col+x) and layout[row+y][col+x] == '#')
        
    return sum(helper(layout, row, col, x, y) for y, x in ADJACENT)


def num_occupied(layout, func, tolerance):
    '''Return number of seats occupied'''
    changed = True

    while changed:
        changed = False
        updated = deepcopy(layout)

        for i, j in product(range(N), range(M)):
            seat = layout[i][j]
            empty = func(layout, i, j)

            if (seat == 'L' and empty == 8) or (seat == '#' and empty <= (8-tolerance)):
                changed = True
                updated[i][j] = '#' if updated[i][j] == 'L' else 'L'

        layout = updated

    return sum(seat == '#' for row in layout for seat in row)


if __name__ == "__main__":
    print(num_occupied(layout, emptyadjacent, 4))
    print(num_occupied(layout, emptyfirst, 5))