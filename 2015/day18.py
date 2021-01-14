'''
from collections import Counter
from itertools import product


with open("inputs/18", "r") as f:
    lights = {complex(x, y) for y, r in enumerate(f) for x, c in enumerate(r) if c=='#'}
    size, turns = 100, 100


def animate(lights: set[complex], corners: set[complex]) -> int:
    ADJACENT = set(complex(x, y) for x, y in product([-1, 0, 1], repeat=2) if not x == y == 0)
    INBOUND = lambda light: 0 <= light.imag < size and 0 <= light.real < size
    
    for _ in range(turns):
        c = Counter(light+delta for light in lights for delta in ADJACENT)
        lights = corners | {k for k, v in c.items() if INBOUND(k) and (v == 3 or (k in lights and v == 2))}

    return len(lights)


if __name__ == "__main__":
    print(animate(lights, set()))
    corners = set(complex(x, y) for x, y in product((0, size-1), repeat=2))
    print(animate(lights|corners, corners))
'''

from collections import Counter
from itertools import product


with open("inputs/18", "r") as f:
    lights = {(y, x) for y, r in enumerate(f) for x, c in enumerate(r) if c=='#'}
    size, turns = 100, 100
    corners = set(product((0, size-1), repeat=2))


def animate(lights: set[tuple], corners: set[tuple]) -> int:
    NEIGHBOR = lambda cube, delta: tuple(x + dx for x, dx in zip(cube, delta))
    ADJACENT = set(product([-1, 0, 1], repeat=2)) - {(0, 0)}
    INBOUND = lambda y, x: 0 <= y < size and 0 <= x < size
    
    for _ in range(turns):
        neighbors = Counter(NEIGHBOR(light, delta) for light in lights for delta in ADJACENT)
        lights = corners | {k for k, v in neighbors.items() if INBOUND(*k) and (v == 3 or (k in lights and v == 2))}

    return len(lights)


if __name__ == "__main__":
    print(animate(lights, set()))
    print(animate(lights|corners, corners))