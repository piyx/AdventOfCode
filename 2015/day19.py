import re
from collections import defaultdict


with open('inputs/19', 'r') as f:
    replacements, medicine = f.read().split('\n\n')


def part1(medicine: str, replacements: str) -> int:
    medicine = re.findall(r'[A-Z][a-z]*', medicine)
    replacement_map = defaultdict(list) # storing replacements as k -> list[rep]
    
    for k, v in map(lambda line: line.split(' => '), replacements.split('\n')):
        replacement_map[k].append(v)
    
    molecules = set()
    for idx, ele in enumerate(medicine):
        if ele not in replacement_map: 
            continue
        
        for i in replacement_map[ele]:
            medicine[idx] = i
            molecules.add(''.join(medicine))
            medicine[idx] = ele
    
    return len(molecules)


def part2(medicine: str, replacements: str) -> int:
    # storing replacements as (v, k) reversed order
    replacements = [(v, k) for k, v in map(lambda s: s.split(' => '), replacements.split('\n'))]
    steps = 0
    while medicine != 'e':
        for v, k in replacements:
            if v in medicine:
                medicine = medicine.replace(v, k, 1)
                steps += 1
    
    return steps


if __name__ == "__main__":
    print(part1(medicine, replacements))
    print(part2(medicine, replacements))