import re
import itertools
import functools


with open("inputs/day05.txt") as f:
    first_section, second_section = f.read().split('\n\n')
    rules = {tuple(map(int, re.findall(r'\d+', line))) for line in first_section.splitlines()}
    updates = [list(map(int, re.findall(r'\d+', line))) for line in second_section.splitlines()]


def is_correct_ordering(rules: set[tuple[int, int]], update: list[int]) -> bool:
    return all((y, x) not in rules for x, y in itertools.combinations(update, 2))


def compare(x: int, y: int) -> int:
    if (x, y) in rules: return -1
    if (y, x) in rules: return 1
    return 0


def get_correct_ordering(update: list[int]) -> list[int]:
    return sorted(update, key=functools.cmp_to_key(compare))


def part1() -> int:
    return sum(update[len(update)//2] for update in updates if is_correct_ordering(rules, update))


def part2():
    return sum(get_correct_ordering(update)[len(update)//2] for update in updates if not is_correct_ordering(rules, update))
    

if __name__=="__main__":
    print(part1())
    print(part2())