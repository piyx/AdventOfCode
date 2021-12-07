import numpy as np

with open("inputs/day7.txt") as f:
    positions = np.array(list(map(int, f.read().split(','))))

median = np.median(positions)
mean = int(np.mean(positions))
triangle = lambda x: x*(x+1)//2
print(np.abs(positions - median).sum())
print(triangle(np.abs(positions - mean)).sum())