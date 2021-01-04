from itertools import groupby


with open('inputs/10', 'r') as f:
    digits = f.read().strip()


def lookandsay(digits, times=40):
    for _ in range(times):
        digits = ''.join(str(len(list(v))) + k for k, v in groupby(digits))
    
    return len(digits)


if __name__ == "__main__":
    print(lookandsay(digits, 40))
    print(lookandsay(digits, 50))