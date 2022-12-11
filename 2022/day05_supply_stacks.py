import re
import copy


with open("inputs/day05.txt") as f:
    starting_stacks, instructions = f.read().split('\n\n')
    instructions = [tuple(map(int, re.findall('\d+', line))) for line in instructions.split('\n')]
    starting_stacks = [line[1::4] for line in starting_stacks.split('\n')[:-1]]
    stacks = [list(''.join(crates).strip())[::-1] for crates in zip(*starting_stacks)]


def move_crates(stacks: list[list[str]], instructions: tuple[int, int, int], move_one_by_one: bool) -> str:
    for num_crates_to_move, src_stack, dest_stack in instructions:
        crates_to_move = [stacks[src_stack-1].pop() for _ in range(num_crates_to_move)]
        crates_ordering = crates_to_move if move_one_by_one else crates_to_move[::-1]
        stacks[dest_stack-1].extend(crates_ordering)
    
    return ''.join(stack[-1] for stack in stacks)


if __name__=="__main__":
    print(move_crates(copy.deepcopy(stacks), instructions, move_one_by_one=True))
    print(move_crates(copy.deepcopy(stacks), instructions, move_one_by_one=False))