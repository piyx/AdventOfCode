import re

passports = []
required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def passport(data):
    passport = {}
    data = data.strip().split()
    for item in data:
        key, val = item.split(':')
        passport[key] = val
    return passport


# reading the input
with open('input.txt', 'r') as f:
    data = ''
    for line in f:
        line = line.strip('\n')
        if line:
            data = data + ' ' + line
        else:
            passports.append(passport(data))
            data = ''
    passports.append(passport(data))


def isvalid(passport):
    return all(field in passport for field in required)


def check(p):
    if not isvalid(p):
        return False

    return all([
        1920 <= int(p['byr']) <= 2002,
        2010 <= int(p['iyr']) <= 2020,
        2020 <= int(p['eyr']) <= 2030,

        (p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][:-2]) <= 193 or
         p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][:-2]) <= 76),

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
