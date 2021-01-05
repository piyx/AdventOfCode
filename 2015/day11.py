import string
import re

with open('inputs/11', 'r') as f:
    password = f.read().strip()
    alphabets = string.ascii_lowercase


def valid(s: str) -> bool:
    return (all(c not in s for c in 'iol') and
            re.search(r'([a-z])\1.*([a-z])\2', s) and
            any(s[i:i+3] in alphabets for i in range(len(s) - 2))
           )


def generate(password: str) -> str:
    password = list(password[::-1])
    
    while True:
        idx, size = 0, len(password)
        while idx < size and password[idx] == 'z':
            password[idx] = 'a'
            idx += 1
        
        if idx == size: password.append('a')
        else: password[idx] = chr(ord(password[idx]) + 1)
        
        yield ''.join(password[::-1])


def renew(password):
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