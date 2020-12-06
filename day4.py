import re


def passport(data):
    return {key: val for item in data.split() for key, val in [item.split(':')]}


# reading the input
with open('inputs/input4.txt', 'r') as f:
    lines = [' '.join(group.split('\n')) for group in f.read().split('\n\n')]
    passports = [passport(line) for line in lines]


def isvalid(passport):
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return all(field in passport for field in required)


REQUIRED = {
    "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
    "iyr": re.compile(r"^20(1[0-9]|20)$"),
    "eyr": re.compile(r"^20(2[0-9]|30)$"),
    "hgt": re.compile(r"^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"),
    "hcl": re.compile(r"^#[0-9a-f]{6}$"),
    "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
    "pid": re.compile(r"^[0-9]{9}$")
}


def check(p):
    return isvalid(p) and all([
        re.match('^19[2-9][0-9]|200[0-2]$', p['byr']),
        re.match('^201[0-9]|2020$', p['iyr']),
        re.match('^202[0-9]|2030$', p['eyr']),
        re.match('^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$', p['hgt']),
        re.match('^#[0-9a-f]{6}$', p['hcl']),
        re.match('amb|blu|brn|gry|grn|hzl|oth', p['ecl']),
        re.match('^[0-9]{9}$', p['pid'])
    ])


def part1(passports):
    return sum(isvalid(passport) for passport in passports)


def part2(passports):
    return sum(check(passport) for passport in passports)


if __name__ == "__main__":
    print(part1(passports))
    print(part2(passports))
