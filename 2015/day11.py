from collections.abc import Iterator
import string
import re

with open('inputs/11', 'r') as f:
    password = f.read().strip()
    alphabets = string.ascii_lowercase


def valid(password: str) -> bool:
    return (all(c not in password for c in 'iol') and
            re.search(r'([a-z])\1.*([a-z])\2', password) and
            any(password[i:i+3] in alphabets for i in range(len(password) - 2))
           )


def generate(password: str) -> Iterator[str]:
    password = list(password[::-1])
    
    while True:
        idx, size = 0, len(password)
        while idx < size and password[idx] == 'z':
            password[idx] = 'a'
            idx += 1
        
        if idx == size: password.append('a')
        else: password[idx] = chr(ord(password[idx]) + 1)
        
        yield ''.join(password[::-1])


def renew(password: str) -> str:
    g = generate(password)
    password = next(g)

    while not valid(password):
        password = next(g)
    
    return password


if __name__ == "__main__":
    part1 = renew(password)
    part2 = renew(part1)
    print(part1)
    print(part2)