import ast
import functools
import itertools


with open("inputs/day13.txt") as f:
    pairs = [tuple(map(ast.literal_eval, pair.splitlines())) for pair in f.read().split('\n\n')]


def compare(left: list, right: list) -> int:
    for l, r in zip(left, right):
        match l, r:
            case int(), int():
                if l < r: return -1
                if l > r: return 1
            case list(), list():
                if (cmp := compare(left=l, right=r)) != 0: return cmp
            case list(), int():
                if (cmp := compare(left=l, right=[r])) != 0: return cmp
            case int(), list():
                if (cmp := compare(left=[l], right=r)) != 0: return cmp

    return -1 if len(left) < len(right) else 1 if len(left) > len(right) else 0


def part1(pairs: list[tuple]) -> int:
    return sum(idx for idx, (l, r) in enumerate(pairs, start=1) if compare(left=l, right=r) == -1)
 

def part2(pairs: list[tuple]) -> int:
    packets = list(itertools.chain(*pairs))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__=="__main__":
    print(part1(pairs))
    print(part2(pairs))