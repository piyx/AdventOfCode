with open("inputs/day01.txt") as f:
    elves_calorie_store = [
        sum(map(int, elf_calorie_input.split('\n')))
        for elf_calorie_input in f.read().strip().split('\n\n')
    ]


def part1(elves_calorie_store: list[int]) -> int:
    return max(elves_calorie_store)


def part2(elves_calorie_store: list[int]) -> int:
    return sum(sorted(elves_calorie_store, reverse=True)[:3])


if __name__=='__main__':
    print(part1(elves_calorie_store))
    print(part2(elves_calorie_store))