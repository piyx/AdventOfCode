with open('data.txt') as f:
    rotations = [(line[0], int(line[1:])) for line in f.read().splitlines()]


def part1(rotations: list[tuple[str, int]]) -> int:
    position = 50
    atzero = 0

    for dir, rotation in rotations:
        match dir:
            case 'R': position = (position+rotation) % 100
            case 'L': position = (position-rotation) % 100
        
        if position == 0: atzero += 1
    
    return atzero


def part2(rotations: list[tuple[str, int]]) -> int:
    position = 50
    crossedzero = 0

    for dir, rotation in rotations:
        wasatzero = position == 0
        crossedzero += rotation // 100
        rotation %= 100

        if rotation == 0: continue
        
        match dir:
            case 'R': position += rotation
            case 'L': position -= rotation
        
        crossedzero += not wasatzero and (position <= 0 or position >= 100) 
        position %= 100
    
    return crossedzero


if __name__=="__main__":
    print(part1(rotations))
    print(part2(rotations))
