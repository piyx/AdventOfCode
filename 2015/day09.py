from itertools import permutations


with open('inputs/9', 'r') as f:
    edges = {frozenset((src, dest)): int(dist) for src, _, dest, _, dist in map(str.split, f)}
    

cities = {city for edge in edges for city in edge}
distances = [sum(edges[frozenset((src, dest))] for src, dest in zip(p[:-1], p[1:])) for p in permutations(cities)]


if __name__ == "__main__":
    print(min(distances))
    print(max(distances))