with open("inputs/day10.txt") as f:
    MAP = {(x+y*1j): int(height) for x, line in enumerate(f.readlines()) for y, height in enumerate(line.strip())}
    STARTHEIGHT = 0
    ENDHEIGHT = 9


def traverse(position: complex):
    reached = []
    queue = [(position, STARTHEIGHT)]

    while queue:
        p, h = queue.pop()
        if p not in MAP: continue
        if h == ENDHEIGHT: reached.append(p)
        queue.extend([(move, h+1) for move in [p+1, p-1, p+1j, p-1j] if move in MAP and MAP[move] == h+1])
    
    return reached


def part1():
    return sum(len(set(traverse(position))) for position in MAP if MAP[position] == STARTHEIGHT)


def part2():
    return sum(len(traverse(position)) for position in MAP if MAP[position] == STARTHEIGHT)


if __name__=="__main__":
    print(part1())
    print(part2())