from math import sqrt
from math import ceil
import itertools


with open('inputs/20') as f:
    presents = int(f.read().strip())


def factors(n: int) -> list[int]:
    f, k = [], sqrt(n)
    for i in range(1, int(k)+1):
        if n%i == 0: f.extend([i, n//i])
    
    if f and f[-1] == k: f.pop()
    return f


part2 = lambda n, i: n >= ceil(i/50)
print(next(i for i in itertools.count(1) if sum(factors(i)) * 10 >= presents))
print(next(i for i in itertools.count(1) if sum(n for n in factors(i) if part2(n, i)) * 11 >= presents))