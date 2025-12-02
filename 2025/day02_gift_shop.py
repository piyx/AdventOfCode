with open("input.txt") as f:
    id_ranges = [(int(lo), int(hi)) for id_range in f.read().split(",") for lo, hi in [id_range.split("-")]]


def is_invalid_id_part1(num: int) -> bool:
    strnum = str(num)
    length = len(strnum)
    return length%2 == 0 and strnum[:length//2] == strnum[length//2:]


def is_invalid_id_part2(num: int) -> bool:
    strnum = str(num)
    length = len(strnum)
    return any(strnum[:i] * (length//i) == strnum for i in range(1, length))    


def part1(id_ranges: list[tuple[int, int]]) -> int:
    return sum(num for lo, hi in id_ranges for num in range(lo, hi+1) if is_invalid_id_part1(num))


def part2(id_ranges: list[tuple[int, int]]) -> int:
    return sum(num for lo, hi in id_ranges for num in range(lo, hi+1) if is_invalid_id_part2(num))


if __name__=="__main__":
    print(part1(id_ranges))
    print(part2(id_ranges))