import re

bags = {}

# reading the input
with open('inputs/input7.txt', 'r') as f:
    for line in f:
        parent = re.match('\w+ \w+', line)[0]
        children = {key: int(val) for val, key in re.findall('(\d+) (\w+ \w+)', line)}
        bags[parent] = children


def contains(child):
    parents = [parent for parent in bags if child in bags[parent]]
    return [child, *[grandparent for parent in parents for grandparent in contains(parent)]]

def required(parent):
    return sum(bags[parent][child] * (1 + required(child)) for child in bags[parent])

def part1(bags):
    return len(set(contains('shiny gold'))) - 1

def part2(bags):
    return required('shiny gold')

if __name__ == "__main__":
    print(part1(bags))
    print(part2(bags))

