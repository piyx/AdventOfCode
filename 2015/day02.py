with open('inputs/2', 'r') as f:
    dimensions = [sorted(map(int, line.split('x'))) for line in f.read().splitlines()]

print(sum(2 * (x*y + y*z + x*z) + x*y for x, y, z in dimensions))
print(sum(2 * (x+y) + (x*y*z) for x, y, z in dimensions))
