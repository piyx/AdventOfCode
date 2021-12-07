from collections import Counter

with open("inputs/day7.txt") as f:
    pos = Counter(map(int, f.read().split(',')))
    beg, end = min(pos), max(pos)

def solve(pos, func=None):
    return min(sum(func(abs(p-dest))*cnts 
               for p, cnts in pos.items())
               for dest in range(beg, end)
            )

print(solve(pos, lambda x: x))
print(solve(pos, lambda x: x*(x+1)//2))