with open("inputs/day3.txt") as f:
    nums = [list(map(int, line.strip())) for line in f.readlines()]
    TwoDArray = list[list[int]]


def most_common(bits: list[int]) -> int:
    return int(sum(bits) >= len(bits)/2)

def least_common(arr: list[int]) -> int:
    return most_common(arr) ^ 1

def binary_to_integer(bits: list[int]) -> int:
    return sum(2**power*bit for power, bit in enumerate(bits[::-1]))

def part1(nums: TwoDArray) -> int:
    most_common_bits = [most_common(column) for column in zip(*nums)]
    least_common_bits = [least_common(column) for column in zip(*nums)]
    gamma_rate = binary_to_integer(most_common_bits)
    epsilon_rate = binary_to_integer(least_common_bits)
    return gamma_rate * epsilon_rate

def part2(nums: TwoDArray) -> int:
    def helper(criteria: callable):
        ratings = nums
        for column_idx in range(len(nums[0])):
            mask = criteria([num[column_idx] for num in ratings])
            ratings = [num for num in ratings if num[column_idx] == mask]
            if len(ratings) == 1: break
        return ratings[0]
    
    o2_generator_rating = binary_to_integer(helper(criteria=most_common))
    co2_scrubber_rating = binary_to_integer(helper(criteria=least_common))
    return o2_generator_rating * co2_scrubber_rating


if __name__=="__main__":
    print(part1(nums))
    print(part2(nums))