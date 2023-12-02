from collections import Counter
import math
import functools
import re


def parse_game(game: str) -> Counter[str, int]:
    gamesets = [
        Counter({color: int(count) for count, color in re.findall(r"(\d+) (\w+)", gameset)})
        for gameset in game.split(":")[1].split(";")
    ]

    return functools.reduce(Counter.__or__, gamesets)


def part1(games: list[Counter[str, int]]) -> int:
    bag = Counter({"red": 12, "green": 13, "blue": 14})
    return sum(gameid for gameid, game in enumerate(games, start=1) if game <= bag)


def part2(games: list[Counter[str, int]]) -> int:
    return sum(math.prod(game.values()) for game in games)


if __name__=="__main__":
    with open("inputs/day02.txt") as f:
        games = [parse_game(game) for game in f.read().splitlines()]
    
    print(part1(games))
    print(part2(games))