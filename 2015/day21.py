from itertools import combinations
from dataclasses import dataclass
from functools import reduce
from math import ceil
import operator
import re


@dataclass
class Player:
    hitpoints: int
    damage: int
    armor: int


@dataclass
class Item:
    cost: int
    damage: int
    armor: int

    def __add__(self, other):
        return Item(self.cost+other.cost,
                    self.damage+other.damage,
                    self.armor+other.armor)


def parse(shop: str) -> list[Item]:
    return [Item(*map(int, re.findall(r'\s(\d+)', item))) for item in shop.splitlines()[1:]]


with open('inputs/21', 'r') as f1, open('inputs/21shop', 'r') as f2:
    boss = Player(*map(int, map(lambda line: line.split(':')[1], f1)))
    weapons, armors, rings = map(parse, f2.read().split('\n\n'))
    armors.append(Item(0, 0, 0))
    rings.append(Item(0, 0, 0))


def solve(weapons: list[Item], armors: list[Item], rings: list[Item]) -> tuple[int, int]:
    choices = (reduce(operator.add, [weapon, armor, r1, r2])
               for weapon in weapons for armor in armors
               for r1, r2 in combinations(rings, 2))

    mincost, maxcost = float("inf"), float("-inf")
    for choice in choices:
        if (ceil(100 / max(boss.damage-choice.armor, 1)) >=
                ceil(boss.hitpoints / max(choice.damage-boss.armor, 1))):

            mincost = min(mincost, choice.cost)

        else:
            maxcost = max(maxcost, choice.cost)

    return mincost, maxcost


if __name__ == "__main__":
    part1, part2 = solve(weapons, armors, rings)
    print(part1)
    print(part2)