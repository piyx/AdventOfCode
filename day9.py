from collections import deque


# reading the input
import time
with open('inputs/input9.txt', 'r') as f:
    nums = [int(line.strip('\n')) for line in f]
    n = len(nums)


def search(nums, target, seen):
    for num in nums:
        if target-num in seen:
            return True
        seen.add(num)

    return False


def part1(nums):
    q = deque(nums[:25])
    for i in range(26, n):
        target = nums[i]
        if not search(q, target, set()):
            return target
        q.popleft()
        q.append(target)


def part2(nums, invalid):
    for i in range(n-1):
        curr = nums[i]
        for j in range(i+1, n):
            if curr == invalid:
                return min(nums[i: j]) + max(nums[i: j])

            curr += nums[j]


if __name__ == "__main__":
    invalid = part1(nums)
    weakness = part2(nums, invalid)
    print(invalid, weakness)
