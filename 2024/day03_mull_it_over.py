import re


with open("inputs/day03.txt") as f:
    memory = f.read().strip()
    


def part1(memory: str) -> int:
    mulpattern = r'mul\((\d+),(\d+)\)'
    return sum(int(x) * int(y) for x, y in re.findall(mulpattern, memory))


def part2(memory: str) -> int:
    pattern = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
    commands = re.findall(pattern, memory) 

    result = 0
    dontmul = False

    for command in commands:
        if command.startswith("don't"): dontmul = True
        elif command.startswith("do"): dontmul = False
        elif command.startswith("mul") and not dontmul:
            x, y = re.findall('\d+', command)
            result += int(x) * int(y)
        
    return result


if __name__=="__main__":
    print(part1(memory))
    print(part2(memory))