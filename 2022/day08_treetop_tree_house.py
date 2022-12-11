with open("inputs/day08.txt") as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])


class Grid:    
    @staticmethod
    def is_visible(grid: list[list[int]], row: int, col: int) -> int:
        if Grid.is_edge(grid, row, col): return True
        return any((
            Grid.is_visible_from_top(grid, row, col),
            Grid.is_visible_from_bottom(grid, row, col),
            Grid.is_visible_from_left(grid, row, col),
            Grid.is_visible_from_right(grid, row, col)
        ))
    
    @staticmethod
    def is_edge(grid: list[list[int]], row: int, col: int) -> bool:
        return row in [0, len(grid)-1] or col in [0, len(grid[0])-1]
    
    @staticmethod
    def is_visible_from_top(grid: list[list[int]], row: int, col: int) -> bool:
        return grid[row][col] > max(grid[r][col] for r in range(row))

    @staticmethod
    def is_visible_from_bottom(grid: list[list[int]], row: int, col: int) -> bool:
        return grid[row][col] > max(grid[r][col] for r in range(row+1, len(grid)))

    @staticmethod
    def is_visible_from_left(grid: list[list[int]], row: int, col: int) -> bool:
        return grid[row][col] > max(grid[row][c] for c in range(col))

    @staticmethod
    def is_visible_from_right(grid: list[list[int]], row: int, col: int) -> bool:
        return grid[row][col] > max(grid[row][c] for c in range(col+1, len(grid[0]))) 


def part1(grid: list[list[int]]) -> int:
    return sum(
        Grid.is_visible(grid, row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
    )


if __name__=="__main__":
    print(part1(grid))