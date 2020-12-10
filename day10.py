from collections import defaultdict, Counter

with open('inputs/input10.txt', 'r') as f:
    ratings = sorted([int(line.strip('\n')) for line in f])


def part1(ratings):
    c = Counter(y-x for x, y in zip([0] + ratings, ratings))
    return c[1] * (c[3] + 1)


def part2(ratings):
    dp = [1] + [0]*(ratings[-1])

    for r in ratings:
        dp[r] = dp[r-1] + dp[r-2] + dp[r-3]

    return dp[-1]


if __name__ == "__main__":
    print(part1(ratings))
    print(part2(ratings))
