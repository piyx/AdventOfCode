import functools


with open("input.txt") as f:
    graph = {ip: op.split() for line in f.readlines() for ip, op in [line.split(":")]}


def part1():
    def dp(node: str, end: str) -> int:
        if node == end: return 1
        return sum(dp(op, end) for op in graph[node])

    return dp('you', 'out')


def part2():
    @functools.cache
    def dp(node: str, end: str) -> int:
        if node == 'out' and end != 'out': return 0
        if node == end: return 1
        return sum(dp(op, end) for op in graph[node])

    return (
        dp('svr', 'fft') * dp('fft', 'dac') * dp('dac', 'out') + 
        dp('svr', 'dac') * dp('dac', 'fft') * dp('fft', 'out')
    )


if __name__=="__main__":
    print(part1())
    print(part2())
