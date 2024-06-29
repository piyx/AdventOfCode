from collections import defaultdict
from itertools import product
import re


def get_adjacent_positions(number: int, row: int, col: int) -> set[tuple[int, int]]:
    deltas = set(product([1, 0, -1], repeat=2)) - {0, 0}
    numlen = len(str(number))
    return {(row+dr, c+dc) for dr, dc in deltas for c in range(col, col+numlen)}


def part1(number_positions: defaultdict[(int, int), int], symbol_positions: defaultdict[(int, int), str]) -> int:        
    return sum(
        number for (row, col), number in number_positions.items()
        if any(adjacent in symbol_positions for adjacent in get_adjacent_positions(number, row, col))
    )




if __name__=="__main__":
    with open("inputs/day03.txt") as f:
        number_positions = defaultdict(int)
        symbol_positions = defaultdict(int)

        for row, line in enumerate(f.read().splitlines()):
            for match in re.finditer(r"\d+", line):
                number_positions[row, match.start()] = int(match.group())
            
            for col, ch in enumerate(line):
                if ch not in ".0123456789": symbol_positions[row, col] = ch

    
    print(number_positions)
    print(symbol_positions)
    print(get_adjacent_positions(114, 0, 5))
    print(part1(number_positions, symbol_positions))