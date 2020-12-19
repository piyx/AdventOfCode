import regex
import re


ISVALID = lambda pattern, message: bool(regex.fullmatch(pattern, message))

with open("inputs/input19.txt", "r") as f:
    ruleset, messages = map(str.splitlines, f.read().split("\n\n"))
    rules = {l: r.strip('"').split() for line in ruleset for l, r in [line.split(": ")]}


def rule_to_regex(rule):
    return f"({''.join(rule_to_regex(r) for r in rules[rule])})" if rule.isdigit() else rule


def part1(rule):
    pattern = rule_to_regex(rule)
    return sum(ISVALID(pattern, message) for message in messages)


def part2(rule):
    rules["8"] = ["(?P<eight>", "42", "|", "42", "(?&eight))"]
    rules["11"] = ["(?P<eleven>", "42", "31", "|", "42", "(?&eleven)", "31", ")"]

    pattern = rule_to_regex(rule)
    return sum(ISVALID(pattern, message) for message in messages)


if __name__ == "__main__":
    print(part1("0"))
    print(part2("0"))
