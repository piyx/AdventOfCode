from collections import Counter
with open("inputs/day6.txt") as f:
    fish = Counter(map(int, f.read().split(',')))


def simulate(fish, iterations=256):
    for _ in range(iterations):
        fish = Counter({k-1: v for k, v in fish.items() if k > 0}) + Counter({6: fish[0], 8: fish[0]})
    return sum(fish.values())


print(simulate(fish, iterations=80))
print(simulate(fish, iterations=256))
