import collections


with open("inputs/day07.txt") as f:
    strengths = {card: idx for idx, card in enumerate(reversed("AKQJT98765432J"))}
    lines = f.read().splitlines()
    hands = []

    for line in lines:
        hand, bid = line.split()
        hands.append((hand, int(bid)))


def handpriority(hand: str) -> int:
    counts = collections.Counter(hand).values()

    match list(sorted(counts)):
        case [5]: return 6                 # five of a kind
        case [1, 4]: return 5              # four of a kind
        case [2, 3]: return 4              # full house
        case [1, 1, 3]: return 3           # three of a kind
        case [1, 2, 2]: return 2           # two pair
        case [1, 1, 1, 2]: return 1        # one pair
        case [1, 1, 1, 1, 1]: return 0     # high card


def handweight(hand: str, allowjoker: bool) -> str:
    priority = handpriority(hand) if not allowjoker else max(handpriority(hand.replace('J', card)) for card in set(hand))
    return 100**5 * priority + sum(100**idx * strengths[card] for idx, card in enumerate(reversed(hand)))


def winnings(hands: list[tuple[int, int]], allowjoker) -> int:
    order = sorted(hands, key=lambda x: handweight(hand=x[0], allowjoker=allowjoker))
    return sum(bid * rank for rank, (hand, bid) in enumerate(order, start=1))


print(winnings(hands, allowjoker=False))
print(winnings(hands, allowjoker=True))