from collections.abc import Iterator
from dataclasses import dataclass
from math import prod
import re


@dataclass
class Ingredient:
    capacity: int = 0
    durability: int = 0
    flavor: int = 0
    texture: int = 0
    calories: int = 0


with open('inputs/15', 'r') as f:
    ingredients = [Ingredient(*map(int, re.findall(r'\d+|-\d+', line))) for line in f]


def bestscore(ingredients: list[Ingredient], T: int, calories: int = None) -> int:
    maxscore = 0
    for quantities in ((w, x, y, T-w-x-y) for w in range(T+1) for x in range(T+1-w) for y in range(T+1-w-x)):
        cookie = Ingredient()
        for q, i in zip(quantities, ingredients):
            cookie.capacity += q * i.capacity
            cookie.durability += q * i.durability
            cookie.flavor += q * i.flavor
            cookie.texture += q * i.texture
            cookie.calories += q * i.calories
        
        values = [cookie.capacity, cookie.durability, cookie.flavor, cookie.texture]
        if all(v >= 0 for v in values) and (not calories or cookie.calories == calories):
            maxscore = max(maxscore, prod(values))
    
    return maxscore


if __name__ == "__main__":
    print(bestscore(ingredients, 100))
    print(bestscore(ingredients, 100, 500))