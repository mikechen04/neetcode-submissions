class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target in matrix:
            return True
        return False