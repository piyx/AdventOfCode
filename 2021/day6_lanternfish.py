with open("inputs/day6.txt") as f:
    cnts = [0]*10
    for num in map(int, f.read().split(',')):
        cnts[num] += 1 


def simulate(cnts, iterations=256):
    for _ in range(iterations):
        copy = [0]*10
        for i in range(1, 10):
            copy[i-1] += cnts[i]
        copy[6] += cnts[0]
        copy[8] += cnts[0]
        cnts = copy
    return sum(cnts)


if __name__=="__main__":
    print(simulate(cnts, iterations=80))
    print(simulate(cnts, iterations=256))
