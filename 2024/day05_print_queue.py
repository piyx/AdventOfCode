from functools import cmp_to_key


def get_correct_ordering(rules: set[tuple[str, str]], update: list[str]) -> list[str]:
    return sorted(update, key=cmp_to_key(lambda x, y: -1 if (x, y) in rules else 1))


with open("inputs/day05.txt") as f:
    rules, updates = f.read().split('\n\n')
    rules = {tuple(line.split('|')) for line in rules.splitlines()}
    part1, part2 = 0, 0

    for update in updates.splitlines():
        update = update.split(',')
        actual = get_correct_ordering(update)
        midpage = int(actual[len(actual)//2])

        if update == actual: part1 += midpage
        else: part2 += midpage
    

if __name__=="__main__":
    print(part1)
    print(part2)