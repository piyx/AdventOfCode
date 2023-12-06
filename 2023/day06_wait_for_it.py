import re
import math


with open("inputs/day06.txt") as f:
    lines = f.read().strip().split('\n')
    times = [int(time) for time in re.findall(r"\d+", lines[0])] 
    distances = [int(dist) for dist in re.findall(r"\d+", lines[1])]    



def num_ways_to_win(time: int, distance: int) -> int:
    lo, hi = 1, time

    while lo < hi:
        mid = (lo+hi) // 2

        if mid * (time-mid) > distance: hi = mid
        else: lo = mid+1    
    
    return time - lo*2 + 1


def part1(times: list[int], distances: list[int]) -> int:
    return math.prod(map(num_ways_to_win, times, distances))

def part2(time: int, distance: int) -> int:
    return num_ways_to_win(time, distance)




time = int(''.join(map(str, times)))
dist = int(''.join(map(str, distances)))

print(part1(times, distances))
print(part2(time, dist))