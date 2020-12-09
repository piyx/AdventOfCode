from collections import deque

with open('inputs/input9.txt', 'r') as f:
    nums = [int(line.strip('\n')) for line in f]


def search(nums, target, seen):
    for num in nums:
        if target-num in seen:
            return True
        seen.add(num)

    return False


def part1(nums):
    q = deque(nums[:25])
    for num in nums[26:]:
        if not search(q, num, set()):
            return num

        q.popleft()
        q.append(num)


def part2(nums, invalid):
    q, s = deque([]), 0
    for num in nums:
        if s == invalid and len(q) > 1:
            return min(q) + max(q)

        s += num
        q.append(num)

        while s > invalid:
            s -= q.popleft()


if __name__ == "__main__":
    invalid = part1(nums)
    weakness = part2(nums, invalid)
    print(invalid, weakness)
