class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
                return 1 # land
            if (i, j) in visit: # already visited
                return 0 # water
            
            visit.add((i, j)) # so we dont visit multiple times
            perim = dfs(i, j + 1) # moving right
            perim += dfs(i + 1, j) # up
            perim += dfs(i, j - 1) # down
            perim += dfs(i - 1, j) # left

            return perim

        for i in range(len(grid)) :
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)
