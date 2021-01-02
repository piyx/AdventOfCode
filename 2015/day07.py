import re
from functools import cache


with open('inputs/7', 'r') as f:
    pattern = r'(\d+|[a-z]+)?\s?([RL]SHIFT|AND|OR|NOT)?\s?(\d+|[a-z]+)? -> ([a-z]+)' 
    data = {rhs: lhs for line in f.readlines() for *lhs, rhs in re.findall(pattern, line)}


bitwise = {'RSHIFT': lambda x, y: solve(x) >> solve(y),
           'LSHIFT': lambda x, y: solve(x) << solve(y),
           'AND': lambda x, y: solve(x) & solve(y),
           'OR': lambda x, y: solve(x) | solve(y),
           'NOT': lambda x, y: ~solve(y),
           '': lambda x, y: solve(x)}


@cache
def solve(start):
    if start.isdigit(): return int(start)
    x, op, y = data[start]
    return bitwise[op](x, y)


if __name__ == "__main__":
    part1 = solve('a')
    solve.cache_clear()
    data['b'] = [str(part1), '', '']
    part2 = solve('a')
    print(part1)
    print(part2)