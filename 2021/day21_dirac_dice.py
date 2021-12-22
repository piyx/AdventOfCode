from collections import Counter, namedtuple
from functools import cache
import itertools
import re

with open("inputs/day21.txt") as f:
    start1, start2 = map(int, re.findall(r": (\d+)", f.read()))
    DICE = itertools.cycle(range(1, 101))
    DIRAC_DICE = Counter(map(sum, itertools.product([1, 2, 3], repeat=3)))
    State = namedtuple('State', ['pos1', 'pos2', 'score1', 'score2', 'turn'])


def roll():
    return sum(next(DICE) for _ in range(3))

def move(state, outcome):    
    pos1, pos2, score1, score2, turn = state
    if turn % 2 == 1:
        pos1 = ((pos1 + outcome) % 10) or 10
        score1 += pos1
    else:
        pos2 = ((pos2 + outcome) % 10) or 10
        score2 += pos2
    return State(pos1, pos2, score1, score2, turn+1)

def part1(state):
    def play(state):
        if state.score1 >= 1000 or state.score2 >= 1000:
            return 3 * state.turn * min(state.score1, state.score2)
        return play(move(state, roll()))
    return play(state)

def part2(state):
    @cache
    def play(state):
        if state.score1 >= 21: return 1
        if state.score2 >= 21: return 1j
        return sum(freq * play(move(state, outcome)) for outcome, freq in DIRAC_DICE.items())

    wins = play(state)
    return int(max(wins.real, wins.imag))


state = State(start1, start2, 0, 0, 1)
print(part1(state))
print(part2(state))