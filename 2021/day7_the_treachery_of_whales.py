import numpy as np

with open("inputs/day7.txt") as f:
    positions = list(map(int, f.read().split(',')))

median = np.median(positions)
mean = int(np.mean(positions))
triangle = lambda x: x*(x+1)//2
print(sum(abs(median-p) for p in positions))
print(sum(triangle(abs(mean-p)) for p in positions))