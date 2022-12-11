import collections
import itertools


with open("inputs/day07.txt") as f:
    terminal_output = f.read().splitlines()
    file_size_limit = 100_000
    total_usable_space = 40_000_000

    path = []
    directory_map = collections.defaultdict(int)

    for line in terminal_output:
        match line.split():
            case ['$', 'cd', '..']: path.pop()
            case ['$', 'cd', dirname]: path.append(dirname)
            case ['$', 'ls']: continue
            case ['dir', _]: continue
            case [filesize, _]:
                for subpath in itertools.accumulate(path, func=lambda a, b: f'{a}/{b}'): 
                    directory_map[subpath] += int(filesize)
    

def part1(directory_map: dict[str, int], file_size_limit: int) -> int:
    return sum(dirsize for dirsize in directory_map.values() if dirsize <= file_size_limit)


def part2(directory_map: dict[str, int], total_usable_space: int) -> int:
    total_space_used = directory_map['/']
    space_to_free = total_space_used - total_usable_space
    return min(dirsize for dirsize in directory_map.values() if dirsize >= space_to_free)


if __name__=="__main__":
    print(part1(directory_map, file_size_limit))
    print(part2(directory_map, total_usable_space))