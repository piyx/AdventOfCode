# Ref: https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnoyy04/

with open("inputs/day8.txt") as f:
    part1 = part2 = 0
    for pattern, output in [line.split('|') for line in f.readlines()]:
        lengths = {len(p): p for p in map(set, pattern.split())}
        
        decoded = ''
        for d in map(set, output.split()):
            match len(d), len(d&lengths[4]), len(d&lengths[2]):
                case 2,_,_: decoded += '1'
                case 3,_,_: decoded += '7'
                case 4,_,_: decoded += '4'
                case 7,_,_: decoded += '8'
                case 5,2,_: decoded += '2'
                case 5,3,1: decoded += '5'
                case 5,3,2: decoded += '3'
                case 6,4,_: decoded += '9'
                case 6,3,1: decoded += '6'
                case 6,3,2: decoded += '0'
        
        part1 += sum(n in '1478' for n in decoded)
        part2 += int(decoded)

print(part1)
print(part2)