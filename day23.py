with open('inputs/input23.txt', 'r') as f:
    data = list(map(int, f.read().strip()))

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def game(data, moves=100, part1=True):
    cups = {}
    dummy = temp = Node(0)
    mincup, maxcup = 1, len(data)

    for val in data:
        temp.next = Node(val)
        cups[val] = temp.next
        temp = temp.next
    
    temp.next, curr = dummy.next, dummy.next

    for _ in range(moves):
        nextcups = [curr.next, curr.next.next, curr.next.next.next]
        curr.next = nextcups[-1].next

        dest = curr.val - 1 or maxcup
        while cups[dest] in nextcups:
            dest = dest - 1 or maxcup

        nextcups[-1].next = cups[dest].next
        cups[dest].next = nextcups[0]

        curr = curr.next
    
    if not part1:
        return cups[1].next.val * cups[1].next.next.val

    ans = ''
    temp = cups[1].next
    while temp != cups[1]:
        ans += str(temp.val)
        temp = temp.next
    
    return ans

if __name__ == "__main__":
    print(game(data, moves=100, part1=True))
    print(game(data + list(range(10, 10**6+1)), moves=10**7, part1=False))