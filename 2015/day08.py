with open('inputs/8', 'r') as f:
    data = f.read().splitlines()

print(sum(len(s) - len(eval(s)) for s in data))
print(sum(2 + s.count('\\') + s.count('"') for s in data))
