class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # so the premise is that we want to use a nested for loop
        # then check every single grid to check if its an island (aka 1)
        # if it is, it has 4 sides, so the perimeter is default 4
        # but then, we check the sides around it, and if any of them are islands as well,
        # then we subtract 2 because two islands together loses each of 1 of their edges
        # then return the perimeter size
        res = 0
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += 4
                    if r and grid[r-1][c]:
                        res -= 2
                    if c and grid[r][c-1] == 1:
                        res -= 2
    
        return res
                    