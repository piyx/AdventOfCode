import collections


with open("inputs/day07.txt") as f:
    strengths = {card: idx for idx, card in enumerate("23456789TJQKA")}
    lines = f.read().splitlines()
    hands = []

    for line in lines:
        hand, bid = line.split()
        hands.append((hand, int(bid)))


def priority(hand: str) -> int:
    counts = collections.Counter(hand).values()

    match list(sorted(counts)):
        case [5]: return 7                 # five of a kind
        case [1, 4]: return 6              # four of a kind
        case [2, 3]: return 5              # full house
        case [1, 1, 3]: return 4           # three of a kind
        case [1, 2, 2]: return 3           # two pair
        case [1, 1, 1, 2]: return 2        # one pair
        case [1, 1, 1, 1, 1]: return 1     # high card


def weight(hand: str, allowjoker: bool) -> list[int]:
    p = priority(hand) if not allowjoker else max(priority(hand.replace('J', card)) for card in set(hand))
    return [p] + [-1 if allowjoker and card == 'J' else strengths[card] for card in hand]


def winnings(hands: list[tuple[int, int]], allowjoker) -> int:
    order = sorted(hands, key=lambda x: weight(hand=x[0], allowjoker=allowjoker))
    return sum(bid * rank for rank, (_, bid) in enumerate(order, start=1))


print(winnings(hands, allowjoker=False))
print(winnings(hands, allowjoker=True))