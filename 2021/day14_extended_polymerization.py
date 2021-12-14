from collections import Counter
import re

with open("inputs/day14.txt") as f:
    polymer, rules = f.read().split('\n\n')
    rules = {k: v for k, v in re.findall(r'([A-Z]+) -> ([A-Z])', rules)}


def pair_insert(poly, rules, steps):
    element_pairs = Counter(prev+curr for prev, curr in zip(poly, poly[1:]))
    element_count = Counter(poly)
    for _ in range(steps):
        for pair, cnt in element_pairs.copy().items():
            mid = rules[pair]
            element_pairs[pair] -= cnt # Remove old pairs
            element_pairs[pair[0]+mid] += cnt 
            element_pairs[mid+pair[1]] += cnt
            element_count[mid] += cnt    
    
    return max(element_count.values()) - min(element_count.values())


print(pair_insert(polymer, rules, steps=10))
print(pair_insert(polymer, rules, steps=40))