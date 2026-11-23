class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    perimeter += 4
                    if row and grid[row-1][col]:
                        perimeter -= 2
                    if col and grid[row][col-1] == 1:
                        perimeter -= 2
        
        return perimeter
        