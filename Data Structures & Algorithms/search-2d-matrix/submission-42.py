class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        pivot = 0

        while l <= r:
            pivot = l + (r-l)//2
            if matrix[pivot][0] > target:
                r = pivot - 1
            else:
                l = pivot + 1
        
        pivot = r
        l, r = 0, len(matrix[0])-1

        while l <= r:
            mid = l + (r-l)//2
            if matrix[pivot][mid] == target:
                return True
            elif matrix[pivot][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False