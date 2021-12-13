from pprint import pprint
import re

with open("inputs/day13.txt") as f:
    data, instructions = f.read().split('\n\n')
    points = {(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', data)}
    folds = [(axis, int(num)) for axis, num in re.findall(r'(x|y)=(\d+)', instructions)]


def after_fold(axis, fold_point, x, y):
    if axis == 'x' and fold_point < x:
        return 2*fold_point-x, y
    elif axis == 'y' and fold_point < y:
        return x, 2*fold_point-y
    return x, y

def perform_fold(points, axis, fold_point):
    return {after_fold(axis, fold_point, x, y) for x, y in points}

def display_paper(points):
    height = max(y for _, y in points) + 1
    widht  = max(x for x, _ in points) + 1
    paper = [[' ']*widht for _ in range(height)]
    for x, y in points:
        paper[y][x] = '#'
    pprint([''.join(row) for row in paper])


part1 = len(perform_fold(points, *folds[0]))
print(part1)

for axis, fold_point in folds:
    points = perform_fold(points, axis, fold_point)

display_paper(points)