class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for i in range(0, len(matrix)):  # top to bottom
            low, high = 0, len(matrix[i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
