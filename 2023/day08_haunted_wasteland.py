import re
import itertools
import math

Network = dict[tuple[str, str], str]


with open("inputs/day08.txt") as f:
    directions, remain = f.read().strip().split("\n\n")
    network = {}

    for line in remain.split("\n"):
        src, left, right = re.findall(r"\w+", line)
        network[src, "L"] = left
        network[src, "R"] = right


def num_steps_required(directions: str, network: Network, src: str, dest: str) -> int:
    steps = 0
    node = src

    for direction in itertools.cycle(directions):
        node = network[node, direction]
        steps += 1

        if node.endswith(dest): return steps


def part1(directions: str, network: Network) -> int:
    return num_steps_required(directions, network, src="AAA", dest="ZZZ")


def part2(directions: str, network: Network) -> int:    
    a_nodes = [node for (node, _) in network if node.endswith("A")]
    steps_required = [num_steps_required(directions, network, a_node, "Z") for a_node in a_nodes]
    return math.lcm(*steps_required)


print(part1(directions, network))
print(part2(directions, network))