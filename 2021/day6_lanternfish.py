from collections import Counter
with open("inputs/day6.txt") as f:
    fish = Counter(map(int, f.read().split(',')))
    print(sum(fish.values()))

def simulate(fish, ndays=256):
    fish = Counter({k: 1 for k in range(6)})
    print(fish)
    for _ in range(ndays):
        if _ % 8 == 0: print("7th", sum(fish.values())) 
        fish = Counter({k-1: v for k, v in fish.items() if k > 0}) + Counter({6: fish[0], 8: fish[0]})
        print(fish, sum(fish.values()))
    return sum(fish.values())


print(simulate(fish, ndays=60))
# print(simulate(fish, ndays=256))