import re
from dataclasses import dataclass


@dataclass
class Reindeer:
    speed: int
    flytime: int
    sleeptime: int
    
    @property
    def cycletime(self):
        return self.flytime + self.sleeptime
    
    def isflying(self, timestamp: int) -> bool:
        return 1 <= (timestamp % self.cycletime) <= self.flytime


with open('inputs/14', 'r') as f:
    deers = [Reindeer(*map(int, re.findall(r'\d+', line))) for line in f]
    totaltime = 2503


def maxdist(deers: list[Reindeer], totaltime: int) -> int:
    ans = 0
    for deer in deers:
        cycles, rem = divmod(totaltime, deer.cycletime)
        curr =  (deer.flytime * cycles + min(rem, deer.flytime)) * deer.speed
        ans = max(ans, curr)
    
    return ans


def maxlead(deers: list[Reindeer], totaltime: int) -> int:
    dist, lead = [0] * len(deers), [0] * len(deers)
    
    for timestamp in range(1, totaltime+1):
        for i, deer in enumerate(deers):
            if deer.isflying(timestamp): dist[i] += deer.speed
        
        currmaxdist = max(dist)
        for i, d in enumerate(dist):
            if d == currmaxdist: lead[i] += 1
    
    return max(lead)


if __name__ == "__main__":
    print(maxdist(deers, totaltime))
    print(maxlead(deers, totaltime))