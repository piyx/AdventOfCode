with open('inputs/1', 'r') as f:
    dirs = [1 if dir == '(' else -1 for dir in f.read().strip()]

print(sum(dirs))
print(next(idx for idx in range(len(dirs)) if sum(dirs[:idx]) == -1))