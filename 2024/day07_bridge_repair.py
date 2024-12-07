from __future__ import annotations
import re
import dataclasses


@dataclasses.dataclass
class Equation:
    result: int
    operands: list[int]

    def _parse(equation: str) -> Equation:
        result, *operands = map(int, re.findall('\d+', equation)) 
        return Equation(result=result, operands=operands)

    def cansolve(self, operations: list[callable]) -> bool:
        results = [self.operands[0]]

        for y in self.operands[1:]:
            results = [func(x, y) for x in results for func in operations]
        
        return self.result in results


with open("inputs/day07.txt") as f:
    EQUATIONS = [Equation._parse(line) for line in f.readlines()]
    ADD = lambda x, y: x+y
    MUL = lambda x, y: x*y
    CAT = lambda x, y: int(f'{x}{y}')


def part1() -> int:
    OPERATIONS = [ADD, MUL]
    return sum(equation.result for equation in EQUATIONS if equation.cansolve(OPERATIONS))


def part2() -> int:
    OPERATIONS = [ADD, MUL, CAT]
    return sum(equation.result for equation in EQUATIONS if equation.cansolve(OPERATIONS))


if __name__=="__main__":
    print(part1())
    print(part2())