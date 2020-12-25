with open('inputs/input25.txt', 'r') as f:
    card, door = map(int, f.read().splitlines())
    sub_num, mod = 7, 20201227

for i in range(mod):
    if pow(sub_num, i, mod) == card:
        print(pow(door, i, mod))
        break