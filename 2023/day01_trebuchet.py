def part1(document: list[str]) -> int:
    total = 0

    for line in document:
        digits = [ch for ch in line if ch.isdigit()]
        total += int(digits[0] + digits[-1])
    
    return total


def part2(document: list[str], words: list[str]) -> int:
    updated_document = [replace_word_with_digit(line, words) for line in document] 
    return part1(updated_document)


def replace_word_with_digit(line: str, words: str) -> str:
    for digit, word in enumerate(words):
        line = line.replace(word, f"{word}{digit}{word}")
    
    return line
        

if __name__=="__main__":
    with open("inputs/day01.txt") as f:
        document = f.read().splitlines()
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    print(part1(document))
    print(part2(document, words))
