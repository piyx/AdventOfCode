'''
--- Part One ---
Specifically, they need you to find the two entries 
that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, 
so the correct answer is 514579.

Of course, your expense report is much larger. Find the 
two entries that sum to 2020; what do you get if you multiply them together?
'''

# reading the input
nums = []
with open("input.txt", 'r') as f:
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


'''
--- Part Two ---
The Elves in accounting are thankful for your help; 
one of them even offers you a starfish coin they had 
left over from a past vacation. They offer you 
a second one if you can find three numbers in your 
expense report that meet the same criteria.

Using the above example again, the three entries that 
sum to 2020 are 979, 366, and 675. Multiplying them 
together produces the answer, 241861950.

In your expense report, what is the product of the 
three entries that sum to 2020?
'''


def part2(nums, target):
    for i, first in enumerate(nums, 1):
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
