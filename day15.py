with open("inputs/input15.txt", "r") as f:
    nums = {int(n): i for i, n in enumerate(f.read().split(","), 1)}


def solve(nums: dict, turns: int) -> int:
    prev = nums.popitem()[0]

    for turn in range(len(nums) + 1, turns):
        nums[prev], prev = turn, turn - nums.get(prev, turn)

    return prev


if __name__ == "__main__":
    print(solve(nums.copy(), 2020))
    print(solve(nums.copy(), 30000000))