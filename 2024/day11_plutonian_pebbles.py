from functools import cache


with open("inputs/day11.txt") as f:
    stones = [int(num) for num in f.read().split()]


@cache
def blink(stone: int, times: int) -> int:
    if times == 0: return 1
    if stone == 0: return blink(1, times-1)

    stonestr = str(stone)
    stonelen = len(stonestr)

    if stonelen%2: return blink(stone*2024, times-1)
    return blink(int(stonestr[:stonelen//2]), times-1) + blink(int(stonestr[stonelen//2:]), times-1)


def part1(stones: list[int]) -> int:
    return sum(blink(stone, times=25) for stone in stones)


def part2(stones: list[int]) -> int:
    return sum(blink(stone, times=75) for stone in stones)


if __name__=="__main__":
    print(part1(stones))
    print(part2(stones))