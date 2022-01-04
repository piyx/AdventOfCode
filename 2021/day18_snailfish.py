from __future__ import annotations
from itertools import combinations
from dataclasses import dataclass
from functools import reduce
from operator import add
import math


@dataclass
class Snailfish:
    val: int = -1
    parent: Snailfish = None
    left: Snailfish = None
    right: Snailfish = None

    def __add__(self, other):
        snailfish = Snailfish(left=self, right=other)
        self.parent = snailfish
        other.parent = snailfish
        
        snailfish.explode()
        while snailfish.split():
            snailfish.explode()
        return snailfish
    
    @staticmethod
    def generate_tree(homework: list[list], parent=None) -> Snailfish:
        if isinstance(homework, int):
            return Snailfish(val=homework, parent=parent)

        node = Snailfish(parent=parent)
        node.left = Snailfish.generate_tree(homework[0], parent=node)
        node.right = Snailfish.generate_tree(homework[1], parent=node)
        return node

    def postorder(self):
        if not self: return

        if self.left: yield from self.left.postorder()
        if self.right: yield from self.right.postorder()
        if self.val != -1: yield self
    
    def add_regular_left_and_right(self, left, right):
        order = list(self.postorder())
        for idx, node in enumerate(order):
            if node is left: break

        n = len(order) - 1
        regular_left = order[idx - 1] if idx > 0 else None
        regular_right = order[idx + 2] if idx < n - 1 else None
        
        if regular_left: regular_left.val += left.val
        if regular_right: regular_right.val += right.val
    
    def explode(self):
        def helper(node, depth=0):
            if not node.left and not node.right: return

            if depth == 4:
                self.add_regular_left_and_right(node.left, node.right)
                node.left = None
                node.right = None
                node.val = 0

            if node.left: helper(node.left, depth + 1)
            if node.right: helper(node.right, depth + 1)

        helper(self)
    
    def split(self):
        if not self: return

        if self.val >= 10:
            half = self.val/2
            self.left = Snailfish(val=math.floor(half), parent=self)
            self.right = Snailfish(val=math.ceil(half), parent=self)
            self.val = -1
            return True

        if self.left and self.left.split(): return True
        if self.right and self.right.split(): return True

    def magnitude(self):
        def helper(node):
            if not node: return 0
            if node.val != -1: return node.val
            return 3*helper(node.left) + 2*helper(node.right)
        return helper(self)


with open("inputs/day18.txt") as f:
    homework = [eval(line.strip()) for line in f.readlines()]

def part1():
    return reduce(add, map(Snailfish.generate_tree, homework)).magnitude()

def part2():
    tree = Snailfish.generate_tree
    max_magnitude = 0
    for h1, h2 in combinations(homework, 2):
        max_magnitude = max(max_magnitude, (tree(h1)+tree(h2)).magnitude())
        max_magnitude = max(max_magnitude, (tree(h2)+tree(h1)).magnitude())
    return max_magnitude

print(part1())
print(part2())