with open('inputs/input8.txt', 'r') as f:
    commands = [[cmd, int(num)] for line in f for cmd,
                num in [line.strip('\n').split()]]


def part1(commands, seen):
    acc, idx = 0, 0

    while idx < len(commands) and idx not in seen:
        seen.add(idx)
        cmd, num = commands[idx]
        idx += num if cmd == 'jmp' else 1
        acc += num if cmd == 'acc' else 0

    return acc, idx


def part2(commands, swap):
    for idx, [cmd, num] in enumerate(commands):
        if cmd == 'acc':
            continue

        commands[idx][0] = swap[cmd]
        acc, pos = part1(commands, set())

        if pos >= len(commands)-1:
            return acc

        commands[idx][0] = cmd


if __name__ == "__main__":
    print(part1(commands, set())[0])
    print(part2(commands, {'jmp': 'nop', 'nop': 'jmp'}))
