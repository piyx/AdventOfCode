# Question link: https://adventofcode.com/2021/day/1

with open("./inputs/day1.txt") as f:
    depths = list(map(int, f.readlines()))

def num_increasing(depths, window_size):
    return sum(new > prev for prev, new in zip(depths, depths[window_size:]))

if __name__=="__main__":
    print(num_increasing(depths, window_size=1))
    print(num_increasing(depths, window_size=3))