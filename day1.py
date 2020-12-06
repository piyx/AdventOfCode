# reading the input
nums = []
with open("inputs/input1.txt", 'r') as f:
    for line in f:
        nums.append(int(line))

target = 2020


def part1(nums, target):
    seen = set()
    for first in nums:
        if (second := target-first) in seen:
            return first*second
        else:
            seen.add(first)


def part2(nums, target):
    for i, first in enumerate(nums[:-2], 1):
        seen = set()
        remain = target - first
        for second in nums[i:]:
            if (third := remain-second) in seen:
                return first*second*third
            else:
                seen.add(second)


if __name__ == "__main__":
    print(part1(nums, target))
    print(part2(nums, target))
