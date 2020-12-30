from sympy.ntheory.modular import crt
from math import prod, ceil


with open('inputs/input13.txt', 'r') as f:
    target = int(next(f))
    buses = {int(bus): -i for i,
             bus in enumerate(next(f).split(',')) if bus != 'x'}


def part1(buses):
    return prod(min((ceil(target/bus) * bus - target, bus) for bus in buses))


def part2(buses):
    return crt(buses.keys(), buses.values())[0]


if __name__ == "__main__":
    print(part1(buses))
    print(part2(buses))
