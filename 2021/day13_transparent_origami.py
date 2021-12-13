from pprint import pprint

with open("inputs/day13.txt") as f:
    data, instructions = f.read().split('\n\n')
    POINTS = {tuple(map(int, line.split(','))) for line in data.splitlines()}
    FOLDS = [
        (axis[-1], int(num))
        for line in instructions.splitlines()
        for axis, num in [line.split('=')]
    ]

def after_fold(axis, f, x, y):
    if axis == 'x':
        return (2*f-x if x > f else x, y)
    return (x, 2*f-y if y > f else y)

for idx, (axis, f) in enumerate(FOLDS):
    POINTS = {after_fold(axis, f, x, y) for x, y in POINTS}
    if idx == 0: print(len(POINTS))

DISPLAY = [[' ']*40 for _ in range(6)]
for x, y in POINTS:
    DISPLAY[y][x] = '#'

pprint([''.join(row) for row in DISPLAY])