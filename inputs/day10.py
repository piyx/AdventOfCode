from collections import defaultdict

with open('inputs/input10.txt', 'r') as f:
    ratings = sorted([int(line.strip('\n')) for line in f])


def part1(ratings):
    diff, prev = defaultdict(int), 0

    for rating in ratings:
        diff[rating-prev] += 1
        prev = rating

    return diff[1] * (diff[3] + 1)


def part2(ratings):
    dp = [1] + [0]*(ratings[-1])

    for r in ratings:
        dp[r] = dp[r-1] + dp[r-2] + dp[r-3]

    return dp[-1]


if __name__ == "__main__":
    print(part1(ratings))
    print(part2(ratings))
