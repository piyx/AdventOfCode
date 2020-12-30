with open('inputs/3', 'r') as f:
    moves = f.read().strip()

MAP = {'<': -1, '>': 1, '^': 1j, 'v': -1j}


def part1(moves):
    santa, homes = 0j, {0j}
    for move in moves:
        santa += MAP[move]
        homes.add(santa)

    return len(homes)


def part2(moves):
    santa, robo, homes = 0j, 0j, {0j}
    for i, j in zip(moves[::2], moves[1::2]):
        santa, robo = santa + MAP[i], robo + MAP[j]
        homes.update({santa, robo})

    return len(homes)


if __name__ == "__main__":
    print(part1(moves))
    print(part2(moves))
