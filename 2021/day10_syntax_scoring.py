with open("inputs/day10.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# CONSTANTS
MATCHIN_TOKENS = {'(': ')', '{': '}', '[': ']', '<': '>'}
INVALID_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
MISSING_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}

part1 = 0
scores = []
for line in lines:
    stack = []
    for token in line:
        if token in MATCHIN_TOKENS:
            stack.append(MATCHIN_TOKENS[token])
        elif not stack or stack.pop() != token:
            part1 += INVALID_POINTS[token]
            break
    else:
        score = 0
        for token in stack[::-1]:
            score = score*5 + MISSING_POINTS[token]
        scores.append(score)

print(part1)
print(sorted(scores)[len(scores)//2])