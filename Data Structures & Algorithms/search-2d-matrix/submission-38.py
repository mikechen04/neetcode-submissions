class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        h = len(matrix)-1

        while l <= h:
            pivot = l + (h-l)//2
            if matrix[pivot][0] > target:
                h = pivot - 1
            else:
                l = pivot + 1

        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[h][mid] == target:
                return True
            elif matrix[h][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        