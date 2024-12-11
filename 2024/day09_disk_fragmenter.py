with open("inputs/day09.txt") as f:
    diskmap = f.read().strip()


def part1(diskmap: str) -> int:
    sequence = [idx//2 if idx%2 == 0 else -1 for idx, length in enumerate(map(int, diskmap)) for _ in range(length)]
    spaces = [pos for pos, fileid in enumerate(sequence) if fileid == -1]
    spaces.reverse()

    for i in range(len(sequence)-1, -1, -1):
        if sequence[i] == -1: continue 
        if i <= spaces[-1]: break
        sequence[spaces.pop()], sequence[i] = sequence[i], -1

    return sum(idx*fileid for idx, fileid in enumerate(sequence) if fileid != -1)


def part2(diskmap: str) -> int:
    files = []
    spaces = []
    position = 0

    for idx, length in enumerate(map(int, diskmap)):
        if idx%2 == 0: files.append((position, length))
        else: spaces.append((position, length))
        position += length
    
    for i in range(len(files)-1, -1, -1):
        _, filelen = files[i]
        for j, (spacepos, spacelen) in enumerate(spaces):
            if i <= j: break
            if spacelen < filelen: continue

            files[i], spaces[j] = (spacepos, filelen), (spacepos+filelen, spacelen-filelen)
            break

    return sum(
        fileid*p 
        for fileid, (filepos, length) in enumerate(files)
        for p in range(filepos, filepos+length)
    )


if __name__=="__main__":
    print(part1(diskmap))
    print(part2(diskmap))
