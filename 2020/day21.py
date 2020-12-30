from collections import defaultdict
import re


with open('inputs/input21.txt', 'r') as f:
    lines = f.read().splitlines()


FOOD = defaultdict(set)
ALL_INGREDS = []
PATTERN = r'(.+)? \(contains (.+)\)'
MAPPING = defaultdict(str)


for line in lines:
    ingrds, alrgns = [set(re.split(' |, ', g)) for g in re.match(PATTERN, line).groups()]
    ALL_INGREDS.extend(ingrds)
    for alrgn in alrgns:
        FOOD[alrgn] = FOOD[alrgn] & ingrds if FOOD[alrgn] else FOOD[alrgn] | ingrds


while FOOD:
    item = [alrgn for alrgn, ingreds in FOOD.items() if len(ingreds) == 1][0]
    ingrd = next(iter(FOOD[item]))
    MAPPING[ingrd] = item
    del FOOD[item]
    for k, v in FOOD.items():
        FOOD[k].discard(ingrd)


SORTED_INGREDS = sorted(MAPPING.keys(), key=lambda x: MAPPING[x])
NO_ALRGNS = [ingrd for ingrd in ALL_INGREDS if ingrd not in MAPPING]


if __name__ == "__main__":
    print(len(NO_ALRGNS))
    print(','.join(SORTED_INGREDS))