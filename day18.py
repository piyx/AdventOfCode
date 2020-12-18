# Full credits to Oliver for this genius solution
from functools import reduce
import re

class Lol:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return Lol(self.x + other.x)
    
    def __sub__(self, other):
        return Lol(self.x * other.x)
    
    def __mul__(self, other):
        return Lol(self.x + other.x)
    
    def __str__(self):
        return str(self.x)

with open('inputs/input18.txt', 'r') as f:
    homework = [re.sub(r"(\d+)", r"Lol(\1)", expr) for expr in f.read().splitlines()]

if __name__ == "__main__":
    print(reduce(lambda x, y: x+y, [eval(expr.replace("*", "-")) for expr in homework]))
    print(reduce(lambda x, y: x+y, [eval(expr.translate(str.maketrans("*+", "-*"))) for expr in homework]))