import ast
import itertools


with open("inputs/day13.txt") as f:
    pairs = [tuple(map(ast.literal_eval, pair.splitlines())) for pair in f.read().split('\n\n')]


def compare(left: list, right: list) -> int:
    for l, r in zip(left, right):
        match l, r:
            case list(), int(): r = [r]
            case int(), list(): l = [l]
            case int(), int() if l < r: return -1
            case int(), int() if l > r: return 1
            case int(), int() if l == r: continue

        if (cmp := compare(l, r)) != 0: return cmp

    if len(left) < len(right): return -1
    if len(left) > len(right): return 1
    return 0
    

def part1(pairs: list[tuple]) -> int:
    return sum(idx for idx, (l, r) in enumerate(pairs, start=1) if compare(left=l, right=r) == -1)
 

def part2(pairs: list[tuple]) -> int:
    divideridx1 = 1 + sum(1 for packet in itertools.chain(*pairs) if compare([[2]], packet) == 1)
    divideridx2 = 2 + sum(1 for packet in itertools.chain(*pairs) if compare([[6]], packet) == 1)
    return divideridx1 * divideridx2


if __name__=="__main__":
    print(part1(pairs))
    print(part2(pairs))