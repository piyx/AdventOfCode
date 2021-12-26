from itertools import product

with open("inputs/day24.txt") as f:
    blocks = [chunk.split('\n') for chunk in f.read().split('inp w\n')[1:]]
    x_adds = [int(block[4].split()[-1]) for block in blocks]
    y_adds = [int(block[14].split()[-1]) for block in blocks]


def run(w_inputs):
    z, w_idx = 0, 0
    ans = [0]*14
    
    for i in range(14):
        x_add, y_add = x_adds[i], y_adds[i]
        
        if x_add > 0:
            z = 26*z + w_inputs[w_idx] + y_add
            ans[i] = w_inputs[w_idx]
            w_idx += 1
        else:
            w = (z % 26) + x_add
            z //= 26
            if not (1 <= w <= 9): return False
            ans[i] = w
    
    return ''.join(map(str, ans))

def part1():
    for w_inputs in product(range(9, 0, -1), repeat=7):
        ans = run(w_inputs) 
        if ans: return ans

def part2():
    for w_inputs in product(range(1, 10), repeat=7):
        ans = run(w_inputs)
        if ans: return ans


print(part1())
print(part2())