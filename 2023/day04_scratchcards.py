from dataclasses import dataclass
from functools import cache
from typing import Self
import re


@dataclass
class Scratchcard:
    winning: set[int]
    numbers: set[int]

    def _parse_card(line: str) -> Self:
        list1, list2 = line.split(":")[-1].strip().split("|")
        
        return Scratchcard(
            winning=set(re.findall(r"\d+", list1)), 
            numbers=set(re.findall(r"\d+", list2))
        )


    def wins(self) -> int:
        return len(self.winning & self.numbers)



def part1(scratchcards: list[Scratchcard]) -> int:
    return sum(int(2 ** (card.wins() - 1)) for card in scratchcards)



def part2(scratchcards: list[Scratchcard]) -> int:
    @cache
    def dp(card: int) -> list[int]:
        wins = scratchcards[card-1].wins()
        cardswon = range(card+1, card+1+wins)
        return 1 + sum(dp(i) for i in cardswon)
    
    return sum(dp(card) for card in range(1, len(scratchcards)+1)) 
        


if __name__=="__main__":
    with open("inputs/day04.txt") as f:
        scratchcards = [Scratchcard._parse_card(line) for line in f.read().splitlines()]
    
    print(part1(scratchcards))
    print(part2(scratchcards))