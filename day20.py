from math import prod, sqrt
from itertools import product


MATCH_BOTTOM = lambda tile1, tile2: tile1[-1] == tile2[0]
MATCH_RIGHT = lambda tile1, tile2: TRANSPOSE(tile1)[-1] == TRANSPOSE(tile2)[0]
REMOVEBORDER = lambda tile: [row[1:-1] for row in tile[1:-1]]
TRANSPOSE = lambda tile: list(map(''.join, zip(*tile)))
BINARY = lambda edge: sum(2**i for i, c in enumerate(edge) if c=="#")
ROTATE = lambda tile: list(map(''.join, zip(*tile[::-1])))
FLIP = lambda tile: list(row[::-1] for row in tile)


MONSTER = ['                  # ', 
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']


def EDGES(tile):
    tp = TRANSPOSE(tile)
    edges = [tp[0], tp[-1], tile[0], tile[-1]]
    return {min(BINARY(e), BINARY(e[::-1])) for e in edges}


def ORIENTATIONS(tile):
        flip = FLIP(tile)
        result = [tile, flip]
        for _ in range(3):
            result.extend([tile:=ROTATE(tile), flip:=ROTATE(flip)])
        
        return result


with open('inputs/input20.txt', 'r') as f:
    data = list(map(str.splitlines, f.read().split('\n\n')))
    borders = {int(block[0][5:-1]): EDGES(block[1:]) for block in data}
    tiles = {int(block[0][5:-1]): ORIENTATIONS(block[1:]) for block in data}


def part1(tiles):
    corners = []
    for tile_id, edges in tiles.items():
        if sum(len(edges & others) == 1 for others in tiles.values()) == 2:
            corners.append(tile_id)

    return prod(corners)

def part2(tiles):
    N = int(sqrt(len(tiles)))
    arranged = [[0]*N for i in range(N)]
    stack = list(list((r, c) for c in range(N) for r in range(N))[::-1])

    def make_image():
        if not stack: return True
        row, col = stack.pop()
        for tile_id, orientations in tiles.copy().items():
            del tiles[tile_id]
            for tile in orientations:
                if row and not MATCH_BOTTOM(arranged[row-1][col][1], tile): continue
                if col and not MATCH_RIGHT(arranged[row][col-1][1], tile): continue
                
                arranged[row][col] = (tile_id, tile)
                if make_image(): return True
            
            tiles[tile_id] = orientations
        stack.append((row, col))

    make_image()
    image = [[REMOVEBORDER(tile[1]) for tile in row] for row in arranged]

    stitched = []
    for row in image:
        stitched.extend(map(''.join, zip(*row)))

    for pattern in ORIENTATIONS(MONSTER):
        n, m, p = len(stitched), len(pattern), len(pattern[0])
        matches = 0
        for dr, dc in product(range(n - m+1), range(n - p+1)):
            matches += all(pattern[r][c] == ' ' or stitched[r + dr][c + dc] == '#'
                            for r in range(m)
                            for c in range(p))
        
        if matches:
            return (''.join(stitched).count('#') - ''.join(pattern).count('#') * matches)

if __name__ == "__main__":
    print(part1(borders))
    print(part2(tiles))