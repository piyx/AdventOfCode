import regex
import re


with open("inputs/input19.txt", "r") as f:
    ruleset, messages = map(str.splitlines, f.read().split("\n\n"))
    rules = {l: r.strip('"').split() for line in ruleset for l, r in [line.split(": ")]}


def regx(rule):
    return f"({''.join(regx(r) for r in rules[rule])})" if rule.isdigit() else rule


if __name__ == "__main__":
    print(sum(bool(re.fullmatch(re.compile(regx("0")), m)) for m in messages))

    rules["8"] = ["(?P<eight>", "42", "|", "42", "(?&eight))"]
    rules["11"] = ["(?P<eleven>", "42", "31", "|", "42", "(?&eleven)", "31", ")"]

    print(sum(bool(regex.fullmatch(regex.compile(regx("0")), m)) for m in messages))