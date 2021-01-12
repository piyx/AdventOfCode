from collections import defaultdict


with open('inputs/17', 'r') as f:
    containers = list(map(int, f.read().splitlines()))
    target, n = 150, len(containers)
    counts = defaultdict(int)


def dfs(idx: int, target: int, used: int) -> int:
    if target == 0:
        counts[used] += 1
        return 1
    
    elif idx >= n or target < 0: 
        return 0
    
    return dfs(idx+1, target-containers[idx], used+1) + dfs(idx+1, target, used)


if __name__ == "__main__":
    print(dfs(0, 150, 0))
    print(counts[min(counts)])