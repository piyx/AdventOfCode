from dataclasses import dataclass
import copy
import math
import re


@dataclass
class Monkey:
    items_in_hand: list[int]
    operation: str
    div_by: int
    if_div_throw_to: int
    if_not_div_throw_to: int
    items_inspected: int = 0


with open("inputs/day11.txt") as f:
    monkeys = []
    for _, items, operation, div_by, if_div, if_not_div in map(str.splitlines, f.read().split('\n\n')):
        monkeys.append(Monkey(
            items_in_hand = list(map(int, re.findall('\d+', items))),
            operation = operation.split('=')[-1].strip(),
            div_by=int(re.search('\d+', div_by).group(0)),
            if_div_throw_to=int(re.search('\d+', if_div).group(0)),
            if_not_div_throw_to=int(re.search('\d+', if_not_div).group(0))
        ))


def simulate_monkey_business(monkeys: list[Monkey], rounds: int, relief_mode: bool) -> int:
    lcm = math.prod((monkey.div_by for monkey in monkeys))

    for _ in range(rounds):
        for monkey in monkeys:            
            for item in monkey.items_in_hand:
                monkey.items_inspected += 1
                worry_level = eval(monkey.operation.replace("old", str(item)))
                worry_level = worry_level // 3 if relief_mode else worry_level % lcm
                throw_to = monkey.if_div_throw_to if worry_level % monkey.div_by == 0 else monkey.if_not_div_throw_to
                monkeys[throw_to].items_in_hand.append(worry_level)

            monkey.items_in_hand = []
    
    items_inspected = [monkey.items_inspected for monkey in monkeys]
    return math.prod(sorted(items_inspected, reverse=True)[:2])


if __name__=="__main__":
    print(simulate_monkey_business(monkeys=copy.deepcopy(monkeys), rounds=20, relief_mode=True))
    print(simulate_monkey_business(monkeys=copy.deepcopy(monkeys), rounds=10_000, relief_mode=False))