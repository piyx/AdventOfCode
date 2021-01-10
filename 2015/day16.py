import re


with open('inputs/16i', 'r') as f1, open('inputs/16ii', 'r') as f2:
    aunts = [{k: int(v) for k, v in re.findall(r'(\w+): (\d+)', line)} for line in f1]
    tape = {k: int(v) for line in f2 for k, v in [line.split(': ')]}
    gt, lt = {'cats', 'trees'}, {'pomeranians', 'goldfish'}


def part1(aunts: list[dict], tape: dict) -> int:
    for i, aunt in enumerate(aunts, 1):
        if all(aunt[k] == tape[k] for k in aunt): 
            return i
    
    return -1


def part2(aunts: list[dict], tape: dict) -> int:
    for i, aunt in enumerate(aunts, 1):
        if all(k not in gt|lt and aunt[k] == tape[k] or
               k in gt and aunt[k] > tape[k] or
               k in lt and aunt[k] < tape[k] for k in aunt): 
        
            return i
    
    return -1


if __name__ == "__main__":
    print(part1(aunts, tape))
    print(part2(aunts, tape))