import re


def parse_mapping(chunk: str) -> list[tuple[int, int, int]]:
    mapping = []

    for line in chunk.split('\n')[1:]:
        dest_start, src_start, length = map(int, re.findall(r"\d+"), line)
        mapping.append((dest_start, src_start, length))
    
    return mapping


with open("inputs/day05.txt") as f:
    seeds, *mappings = f.read().split('\n\n')
    initial_seeds = [int(seed) for seed in re.findall(r"\d+", seeds)]
    mappings = [parse_mapping(mapping) for mapping in mappings]


def part2(seed_ranges: list[int], mappings: list[list[tuple[int, int, int]]]) -> int:
    transformed_seed_ranges = []

    for mapping in mappings:
        transformed_seed_ranges = []
        while seed_ranges:
            seed_start, seed_end = seed_ranges.pop()
            
            for dest_start, src_start, length in mapping:
                overlap_start = max(src_start, seed_start)
                overlap_end = min(src_start+length, seed_end)

                if overlap_start < overlap_end: # There is overlap
                    transformed_seed_ranges.append((overlap_start, overlap_end))
                
                    if seed_start < overlap_start: # Non overlap left side
                        seed_ranges.append((seed_start, overlap_start-1))
                    
                    if seed_end > overlap_end: # Non overlap right side
                        seed_ranges.append((overlap_end+1, seed_end))
                    
                
                else:
                    seed_ranges.append((seed_start, seed_end))



'''

   50  1000
20    70


   50    1000
      70       200

    50      1000
      70  100


     50  1000

20 30


    50 1000
             30 40
''' 