from math import prod, sqrt

class Tile:
    @staticmethod
    def rotate(tile):
        return list(map(''.join, zip(*tile[::-1])))
    
    @staticmethod
    def transpose(tile):
        return list(map(''.join, zip(*tile)))
    
    @staticmethod
    def flip(tile):
        return list(row[::-1] for row in tile)
    
    @staticmethod
    def binary(edge):
        return sum(2**i for i, c in enumerate(edge) if c=="#")
    
    @staticmethod
    def removeborder(tile):
        return [row[1:-1] for row in tile[1:-1]]
    
    @staticmethod
    def edges(tile):
        tp = Tile.transpose(tile)
        edges = [tp[0], tp[-1], tile[0], tile[-1]]
        return {min(Tile.binary(e), Tile.binary(e[::-1])) for e in edges}
    
    @staticmethod
    def orientations(tile):
        flip = Tile.flip(tile)
        result = [tile, flip]
        for _ in range(3):
            result.extend([tile:=Tile.rotate(tile), flip:=Tile.rotate(flip)])
        
        return result


with open('inputs/input20.txt', 'r') as f:
    data = list(map(str.splitlines, f.read().split('\n\n')))
    print(len(data))
    borders = {int(block[0][5:-1]): Tile.edges(block[1:]) for block in data}
    tiles = {int(block[0][5:-1]): Tile.orientations(block[1:]) for block in data}


def part1(tiles):
    corners = []
    for tile_id, edges in tiles.items():
        if sum(len(edges & others) == 1 for others in tiles.values()) == 2:
            corners.append(tile_id)

    return prod(corners)

N = int(sqrt(len(tiles)))
arranged = [[0]*N for i in range(N)]
stack = list(list((r, c) for c in range(N) for r in range(N))[::-1])

def make_image():
    if not stack: return True
    r, c = stack.pop()
    for tile_id, orientations in tiles.copy().items():
        del tiles[tile_id]
        for tile in orientations:
            if r > 0 and arranged[r-1][c][1][-1] != tile[0]: continue
            if c > 0 and [row[-1] for row in arranged[r][c-1][1]] != [row[0] for row in tile]: continue
            arranged[r][c] = (tile_id, tile)
            if make_image(): return True
        
        tiles[tile_id] = orientations
    stack.append((r, c))

make_image()


image = [[Tile.removeborder(tile[1]) for tile in row] for row in arranged]
tile_n = len(image[0][0])


def get(r, c):
    return image[r // tile_n][c // tile_n][r % tile_n][c % tile_n]


image = [''.join(get(r, c) for c in range(N * tile_n)) for r in range(N * tile_n)]

MONSTER = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']

for pattern in Tile.orientations(MONSTER):
    matches = 0
    for dr in range(len(image) - len(pattern) + 1):
        for dc in range(len(image[0]) - len(pattern[0]) + 1):
            matches += all(pattern[r][c] == ' ' or image[r + dr][c + dc] == '#'
                           for r in range(len(pattern))
                           for c in range(len(pattern[0])))
    if matches:
        print(''.join(image).count('#') -
              ''.join(pattern).count('#') * matches)
        break