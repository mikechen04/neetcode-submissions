class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for i in range(0, len(matrix)):  # top to bottom
            #looping through each row so each iteration within this loop is checking each colum
            low, high = 0, len(matrix[i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target: #then it means the target is more towards the right
                    low = mid + 1
                else: #if the value of target is lower then it must be on the left
                    high = mid - 1
        return False
