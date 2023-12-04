from dataclasses import dataclass
from functools import cache
from typing import Self
import re


@dataclass
class Scratchcard:
    winning_numbers: set[int]
    my_numbers: set[int]

    def _parse_card(line: str) -> Self:
        _, numbers = line.split(":")
        list1, list2 = numbers.strip().split("|")
        
        return Scratchcard(
            winning_numbers=set(re.findall(r"\d+", list1)), 
            my_numbers=set(re.findall(r"\d+", list2))
        )


    def wins(self) -> int:
        return len(self.winning_numbers & self.my_numbers)



def part1(scratchcards: list[Scratchcard]) -> int:
    return sum(int(2 ** (card.wins() - 1)) for card in scratchcards)



def part2(scratchcards: list[Scratchcard]) -> int:
    @cache
    def dp(card_num: int) -> list[int]:
        wins = scratchcards[card_num-1].wins()
        cards_won = range(card_num+1, card_num+1+wins)
        return 1 + sum(dp(i) for i in cards_won)
    
    return sum(dp(card_num) for card_num in range(1, len(scratchcards)+1)) 
        


if __name__=="__main__":
    with open("inputs/day04.txt") as f:
        scratchcards = [Scratchcard._parse_card(line) for line in f.read().splitlines()]
    
    print(part1(scratchcards))
    print(part2(scratchcards))