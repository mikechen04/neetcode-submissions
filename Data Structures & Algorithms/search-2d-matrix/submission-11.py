class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            l, h = 0, len(matrix[i]) - 1
            while l <= h:
                mid = (l + h) // 2
                if matrix[i][mid] == target:  #matrix[row][column]
                    return True
                if matrix[i][mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
       
        return False
