import dataclasses
from typing import Self


@dataclasses.dataclass
class Section:
    start: int
    end: int

    @classmethod
    def fromstring(cls, section: str) -> Self:
        return Section(*map(int, section.split('-')))
    
    def is_complete_overlap(self, other: Self) -> bool:
        return self.start <= other.start and self.end >= other.end
    
    def is_overlap(self, other: Self) -> bool:
        return self.start <= other.start <= self.end or other.start <= self.start <= other.end


with open("inputs/day04.txt") as f:
    section_assignment_pairs = [
        (Section.fromstring(left_section), Section.fromstring(right_section))
        for pair in f.read().splitlines()
        for left_section, right_section in [pair.split(',')]
    ]


def part1(section_assignment_pairs: list[tuple[Section, Section]]) -> int:
    return sum(
        left_section.is_complete_overlap(right_section) or 
        right_section.is_complete_overlap(left_section)
        for left_section, right_section in section_assignment_pairs
    )


def part2(section_assignment_pairs: list[tuple[Section, Section]]) -> int:
    return sum(
        left_section.is_overlap(right_section)
        for left_section, right_section in section_assignment_pairs
    )


if __name__=="__main__":
    print(part1(section_assignment_pairs))
    print(part2(section_assignment_pairs))