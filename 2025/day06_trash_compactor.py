import math


with open("input.txt") as f:
    lines = f.readlines()


def part1():    
    rows = [list(map(int, row.strip().split())) for row in lines[:-1]]
    cols = list(zip(*rows))
    operators = lines[-1].split()

    return sum(
        math.prod(operands) if operator == '*' else sum(operands)
        for operands, operator in zip(cols, operators)
    )


def part2():
    operators = iter(lines[-1].split())
    cols = list(zip(*lines[:-1]))
    result = 0
    operands = []

    for col in cols:
        num = ''.join(col).strip()
        
        if num.isdigit():
            operands.append(int(num))
            continue

        operator = next(operators)
        result += math.prod(operands) if operator == '*' else sum(operands)
        operands.clear()

    return result


if __name__=="__main__":
    print(part1())
    print(part2())
