import hashlib
import itertools

with open('inputs/4', 'r') as f:
    key = f.read().strip()


def starts_with_n_zeroes(n=5):
    for num in itertools.count():
        newkey = (key + str(num)).encode()
        if hashlib.md5(newkey).hexdigest()[:n] == '0'*n:
            return num

if __name__ == "__main__":
    print(starts_with_n_zeroes(n=5))
    print(starts_with_n_zeroes(n=6))