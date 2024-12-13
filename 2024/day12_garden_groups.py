with open("inputs/day12.txt") as f:
    GARDEN = {x+y*1j: plant for x, line in enumerate(f.readlines()) for y, plant in enumerate(line.strip())}
    GROUPS = []    
    seen = set()

    for position, plant in GARDEN.items():
        if position in seen: continue

        group = {position}
        queue = [position]
        
        while queue:
            position = queue.pop()
            if GARDEN.get(position) != plant: continue 
            
            group.add(position)
            seen.add(position)
            queue.extend(position+d for d in [-1, 1j, 1, -1j] if position+d not in group)
        
        GROUPS.append(group)


def area(group: set[complex]) -> int:
    return len(group)


def perimeter(group: set[complex]) -> int:
    return sum(p+d not in group for p in group for d in [-1, 1j, 1, -1j])


def sides(group: set[complex]) -> int:
    return sum(
        (p+dx not in group and p+dy not in group) +                 # outside corner
        (p+dx in group and p+dy in group and p+dx+dy not in group)  # inside corner
        for p in group 
        for dx, dy in [(-1, 1j), (1j, 1), (1, -1j), (-1j, -1)]
    )


def part1() -> int:
    return sum(area(group) * perimeter(group) for group in GROUPS)


def part2() -> int:
    return sum(area(group) * sides(group) for group in GROUPS)


if __name__=="__main__":
    print(part1())
    print(part2())