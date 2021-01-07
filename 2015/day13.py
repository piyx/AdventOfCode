import re
from itertools import permutations
from collections import defaultdict


with open('inputs/13', 'r') as f:
    data = [re.findall(r'^(\w+).*(gain|lose).*\b(\d+).*\b(\w+)\.$', line)[0] for line in f]
    happiness, attendees = defaultdict(int), set()
    

for name1, sign, units, name2 in data:
    happiness[name1, name2] = int(units if sign == 'gain' else f'-{units}')
    attendees |= {name1, name2}


def optimal_seating(happiness: dict, attendees: set) -> int:
    return max(sum(happiness[x, y] + happiness[y, x] for x, y in zip(p[1:] + p[:1], p)) for p in permutations(attendees))


if __name__ == "__main__":
    print(optimal_seating(happiness, attendees))
    print(optimal_seating(happiness, attendees|{'me'}))