from collections import defaultdict
from math import prod


with open("inputs/input16.txt", "r") as f:
    field_data, myticket, nearby = [sub.splitlines() for sub in f.read().split("\n\n")]

    fields = {}
    for line in field_data:
        field, rule = line.split(":")
        fields[field] = [tuple(map(int, r.split("-"))) for r in rule.split("or")]

    nearby = [list(map(int, line.split(","))) for line in nearby[1:]]
    myticket = [int(num) for num in myticket[1].split(",")]


def isvalidnum(fields, num):
    return any(left <= num <= right for f in fields for left, right in fields[f])


def isvalid_ticket(fields, ticket):
    return all(isvalidnum(fields, num) for num in ticket)


def part1(fields, nearby):
    return sum(n for ticket in nearby for n in ticket if not isvalidnum(fields, n))


def part2(fields, nearby, myticket):
    valid = [ticket for ticket in nearby if isvalid_ticket(fields, ticket)]
    transpose = list(zip(*valid))

    mapping = defaultdict(set)
    for i, column in enumerate(transpose):
        for field, rules in fields.items():
            if all(any(l <= num <= r for l, r in rules) for num in column):
                mapping[i].add(field)

    order = defaultdict(str)
    while mapping:
        idx = next(idx for idx, s in mapping.items() if len(s) == 1)
        order[idx] = next(iter(mapping[idx]))
        for _, s in mapping.items():
            s.discard(order[idx])

        del mapping[idx]

    return prod(myticket[idx] for idx, field in order.items() if "departure" in field)


if __name__ == "__main__":
    print(part1(fields, nearby))
    print(part2(fields, nearby, myticket))
