with open("input.txt") as f:
    ranges, ingredients = f.read().split('\n\n')
    freshranges = [(int(lo), int(hi)) for line in ranges.splitlines() for lo, hi in [line.split("-")]]
    ingredients = list(map(int, ingredients.splitlines()))


def part1():
    return sum(any(lo <= ing <= hi for lo, hi in freshranges) for ing in ingredients)


def part2():
    fresh, prev = 0, 0

    for lo, hi in sorted(freshranges):
        if prev > hi: continue
        fresh += hi-max(lo, prev)+1
        prev = hi+1

    return fresh


if __name__=="__main__":
    print(part1())
    print(part2())
