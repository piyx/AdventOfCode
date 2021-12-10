import itertools

with open("inputs/day4.txt") as f:
    random_draws = list(map(int, next(f).strip().split(',')))
    next(f)
    boards = [[list(map(int, line.split())) 
              for line in board.split('\n')]
              for board in f.read().split("\n\n")]
    
    ThreeDArray = list[list[list[int]]]


def isbingo(board: ThreeDArray, random_draw: int) -> bool:
    # Finding the position of the random_draw and marking it as True
    for row, col in itertools.product(range(5), range(5)):
        if board[row][col] == random_draw:
            board[row][col] = True
            break

    # Checking if the random_draw has lead to a win or not
    horizontal = all(board[row][c] == True for c in range(5))
    vertical = all(board[r][col] == True for r in range(5))
    return horizontal or vertical

def board_score(board: ThreeDArray, final_draw: int) -> int:
    undrawn = [num for row in board for num in row if num != True]
    return sum(undrawn) * final_draw

def simulate(random_draws: list[int], boards: ThreeDArray) -> int:
    part1 = None
    part2 = None

    boards_won = set()

    for random_draw in random_draws:
        for board_idx, board in enumerate(boards):
            if board_idx in boards_won: continue
            if isbingo(board, random_draw):
                if part1 is None:
                    part1 = board_score(board, random_draw)
                
                boards_won.add(board_idx)
                if len(boards_won) == len(boards):
                    part2 = board_score(board, random_draw) 
    
    return part1, part2


if __name__=="__main__":
    part1, part2 = simulate(random_draws, boards)
    print(part1)
    print(part2)