from collections import deque
from itertools import islice

with open("inputs/input22.txt", "r") as f:
    first, second = map(str.splitlines, f.read().split('\n\n'))
    p1, p2 = deque(map(int, first[1:])), deque(map(int, second[1:]))

SCORE = lambda cards: sum(i*card for i, card in enumerate(reversed(cards), 1))

def part1(p1, p2):
    while p1 and p2:
        one, two = p1.popleft(), p2.popleft()
        if one > two: p1.extend([one, two])
        else: p2.extend([two, one])
    
    return p1 or p2

def recursive_combat(p1, p2):
    seen = set()
    while p1 and p2:
        if (prev:= (tuple(p1), tuple(p2))) in seen: return True
        seen.add(prev)

        one, two = p1.popleft(), p2.popleft()
        if len(p1) >= one and len(p2) >= two:
            result = recursive_combat(deque(islice(p1, one)), deque(islice(p2, two)))

            if result: p1.extend([one, two])
            else: p2.extend([two, one])
            
            continue
            
        if one > two: p1.extend([one, two])
        else: p2.extend([two, one])
    
    return bool(p1)

def part2(p1, p2):
    return p1 if recursive_combat(p1, p2) else p2

if __name__ == "__main__":
    print(SCORE(part1(p1.copy(), p2.copy())))
    print(SCORE(part2(p1.copy(), p2.copy())))


