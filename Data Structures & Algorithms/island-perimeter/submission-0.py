class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        solution = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    add = 4
                    if row > 0 and grid[row - 1][col] == 1:
                        add -= 1
                    if col > 0 and grid[row][col - 1] == 1:
                        add -= 1
                    if row < rows - 1 and grid[row + 1][col] == 1:
                        add -= 1
                    if col < cols - 1 and grid[row][col + 1] == 1:
                        add -= 1
                    solution += add

        return solution