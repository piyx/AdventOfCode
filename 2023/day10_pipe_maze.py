with open("inputs/day10.txt") as f:
    maze = {
        (row, col): pipe
        for row, line in enumerate(f.read().splitlines())
        for col, pipe in enumerate(line)
    }

    directions = "NEWS"
    moves = {
        ("|", "S"): (1, 0),
        ("|", "N"): (-1, 0),
        ("-", "E"): (0, 1),
        ("-", "W"): (0, -1),
        ("L", "S"): (1, 1),
        ("L", "E"): (-1, -1),
        ("J", "S"): (1, -1),
        ("J", "E"): (-1, 1),
        ("F", "W"): (1, -1),
        ("F", "N"): (-1, 1),
    }


Maze = dict[tuple[int, int], str]


def loop_length(row: int, col: int, maze: Maze) -> int:
    pass
    

def part1(maze: Maze) -> int:
    import time
    start_row, start_col = next((row, col) for (row, col), pipe in maze.items() if pipe == "S")
    row, col = start_row+1, start_col

    loopsize = 0
    print(start_row, start_col, row, col)
    visited = {(start_row, start_col)}

    while (row, col) != (start_row, start_col):
        for direction in directions:
            pipe = maze.get((row, col), ".")
            print(pipe, direction, row, col)


            if (pipe, direction) in moves:
                visited.add((row, col))
                print(visited)
                
                r, c = moves[pipe, direction]

                if (row+r, col+c) in visited: continue

                row, col = row+r, col+c
                print(row, col)
                loopsize += 1


                time.sleep(0.5)
        
            time.sleep(1)
    
    return loopsize // 2


print(maze)
print(part1(maze))