# Question link: https://adventofcode.com/2021/day/2
# Reference: github.com/salt-die

import re

with open("inputs/day2.txt") as f:
    commands = [(direction, int(step)) for direction, step in re.findall(r"(\w+) (\d+)", f.read())]

def part1(commands):
    left, down = 0, 0
    
    for direction, step in commands:
        match direction:
            case "forward":
                left += step
            case "down":
                down += step
            case "up":
                down -= step
    
    return left*down

def part2(commands):
    aim, right, down = 0, 0, 0
    
    for direction, step in commands:
        match direction:
            case "forward":
                right += step
                down += aim*step
            case "down":
                aim += step
            case "up":
                aim -= step
    
    return right*down

if __name__=="__main__":
    print(part1(commands))
    print(part2(commands))