# Credits https://github.com/MasterMedo

import re
from itertools import product
from collections import defaultdict

with open("inputs/input14.txt", "r") as f:
    lines = f.read().splitlines()

BINARY = lambda n: bin(int(n))[2:].zfill(36)
PART = lambda mem: sum(mem.values())

MEM1 = defaultdict(int)
MEM2 = defaultdict(int)


def bitmask(mask, num):
    return "".join(
        num_bit if mask_bit == "X" else mask_bit for mask_bit, num_bit in zip(mask, num)
    )


def floating_bitmask(mask, address):
    for f in map(iter, product("10", repeat=mask.count("X"))):
        new_address = "".join(
            next(f) if mask_bit == "X" else "1" if mask_bit == "1" else address_bit
            for mask_bit, address_bit in zip(mask, address)
        )
        yield new_address


for line in lines:
    if line.startswith("mask"):
        mask = line[7:]
        continue

    address, num = map(BINARY, re.findall("\d+", line))
    MEM1[address] = int(bitmask(mask, num), 2)

    for new_address in floating_bitmask(mask, address):
        MEM2[new_address] = int(num, 2)


if __name__ == "__main__":
    print(PART(MEM1))
    print(PART(MEM2))
