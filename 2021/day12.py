from collections import defaultdict

with open("inputs/day12.txt") as f:
    GRAPH = defaultdict(list)
    for line in f.read().splitlines():
        u, v = line.split("-")
        GRAPH[u].append(v)
        GRAPH[v].append(u)


def dfs(node, path, revisited):
    if node == "end": return 1

    num_paths = 0
    new_path  = path | {node}
    
    for neib in GRAPH[node]:
        if neib == "start": 
            continue
        elif neib.isupper() or neib not in path:
            num_paths += dfs(neib, new_path, revisited)
        elif not revisited:
            num_paths += dfs(neib, new_path, True)
    
    return num_paths


print(dfs("start", set(), True))
print(dfs("start", set(), False))