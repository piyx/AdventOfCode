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


if __name__ == "__main__":
    print(len(set(contains('shiny gold'))) - 1)  # part1
    print(required('shiny gold'))                # part2
