with open("input.txt") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]


def largest_ndigit_number(sequence: list[int], ndigits: int) -> int:
    result, position = 0, 0

    for d in range(1, ndigits+1):
        maxdigit, maxindex = 0, 0

        for i in range(position, len(sequence)-ndigits+d):
            if sequence[i] <= maxdigit: continue
            maxdigit = sequence[i]
            maxindex = i
        
        result = result*10 + maxdigit
        position = maxindex+1

    return result


def part1(grid: list[list[int]]) -> int:
    return sum(largest_ndigit_number(row, ndigits=2) for row in grid)


def part2(grid: list[list[int]]) -> int:
    return sum(largest_ndigit_number(row, ndigits=12) for row in grid)


if __name__=="__main__":
    print(part1(grid))
    print(part2(grid))
