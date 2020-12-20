import regex


with open("inputs/input19.txt", "r") as f:
    ruleset, messages = map(str.splitlines, f.read().split("\n\n"))
    rules = {l: r.strip('"').split() for line in ruleset for l, r in [line.split(": ")]}
    updates = {'8' : '(?P<rule8> 42 | 42 (?&rule8))'.split(),
               '11': '(?P<rule11> 42 31 | 42 (?&rule11) 31 )'.split()}


def rule_to_regex(rules, rule):
    return f"({''.join(rule_to_regex(rules, r) for r in rules[rule])})" if rule.isdigit() else rule


if __name__ == "__main__":
    TOTAL = lambda pattern: sum(bool(regex.fullmatch(pattern, message)) for message in messages)
    pattern1 = rule_to_regex(rules, '0')
    pattern2 = rule_to_regex(rules|updates, '0')
    print(TOTAL(pattern1))
    print(TOTAL(pattern2))