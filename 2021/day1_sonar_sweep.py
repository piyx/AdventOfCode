# Question link: https://adventofcode.com/2021/day/1

with open("./inputs/day1.txt") as f:
    depths = list(map(int, f.readlines()))

def part1(depths):
    return sum((new > prev) for prev, new in zip(depths, depths[1:]))


def part2(depths):
    window_depth = 3
    window_sum = sum(depths[:3])

    window_sums = [window_sum]
    for idx in range(3, len(depths)):
        window_sum += depths[idx]
        window_sum -= depths[idx-window_depth]
        window_sums.append(window_sum)

    return part1(window_sums)


if __name__=="__main__":
    print(part1(depths))
    print(part2(depths))