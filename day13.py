from math import prod, ceil, lcm


with open('inputs/input13.txt', 'r') as f:
    target = int(next(f))
    busses = [(int(bus), i) for i, bus in enumerate(
        next(f).split(','), 0) if bus != 'x']


def part1(busses):
    return prod(min((ceil(target/bus) * bus - target, bus) for bus, i in busses))


def part2(busses):
    num = 0
    curr_lcm = 1
    for x, y in busses:
        while -num % x != y % x:
            num += curr_lcm
        curr_lcm = lcm(curr_lcm, x)
    return num


if __name__ == "__main__":
    print(part1(busses))
    print(part2(busses))
