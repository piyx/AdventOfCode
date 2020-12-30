with open('inputs/input12.txt', 'r') as f:
    data = [(line[0], int(line[1:].strip('\n'))) for line in f]


MAP = {'N': +1j, 'S': -1j, 'E': 1, 'W': -1, 'R': -1j, 'L': 1j}
ROTATE = lambda dir, deg: MAP[dir]**(deg//90)
MOVE = lambda dir, dist: dir*dist


def part1(data):
    xy, d = 0, 1
    for D, N in data:
        if D == 'F': xy += d*N
        elif D in 'RL': d *= ROTATE(D, N)
        else: xy += N*MAP[D]
    
    return abs(xy.real) + abs(xy.imag)


def part2(data):
    xy, wp = 0, 10 + 1j
    for D, N in data:
        if D == 'F': xy += MOVE(wp, N)
        elif D in 'RL': wp *= ROTATE(D, N)
        else: wp += N*MAP[D]
    
    return abs(xy.real) + abs(xy.imag)

if __name__ == "__main__":
    print(part1(data)) 
    print(part2(data))