import string
import functools


with open("inputs/day03.txt") as f:
    rucksacks = f.read().splitlines()
    priorities = {letter: priority for priority, letter in enumerate(string.ascii_letters, start=1)}


def get_common_item(*sets: tuple[set[str]]) -> str:
    return functools.reduce(set.intersection, sets).pop()


def part1(rucksacks: list[str]) -> int:
    common_letters = []

    for rucksack in rucksacks:
        half_size = len(rucksack) // 2
        first_half = set(rucksack[:half_size])
        second_half = set(rucksack[half_size:])
        common_letters.append(get_common_item(first_half, second_half))    
    
    return sum(map(priorities.get, common_letters))


def part2(rucksacks: list[str]) -> int:
    common_letters = []
    group_size = 3

    for idx in range(0, len(rucksacks), group_size):
        group = map(set, rucksacks[idx: idx+group_size])
        common_letters.append(get_common_item(*group))

    return sum(map(priorities.get, common_letters))
    

if __name__=="__main__":
    print(part1(rucksacks))
    print(part2(rucksacks))