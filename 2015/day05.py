import re


with open('inputs/5', 'r') as f:
    strings = f.read().splitlines()
    rules1 = [r'^((?!ab|cd|pq|xy).)*$', r'([a-z])\1', r'([aeiou].*){3}']
    rules2 = [r'([a-z]{2}).*\1', r'([a-z]).\1']


def ishappy(string, rules):
    return all(re.search(rule, string) for rule in rules)


if __name__ == "__main__":
    print(sum(ishappy(string, rules1) for string in strings))
    print(sum(ishappy(string, rules2) for string in strings))