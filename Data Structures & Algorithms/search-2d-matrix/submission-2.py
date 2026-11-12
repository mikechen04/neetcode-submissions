class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        n = len(matrix)

        while l <= h:
            mid = (l + h) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return False



