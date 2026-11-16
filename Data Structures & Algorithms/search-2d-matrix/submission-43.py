class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid][0] > target:
                r = mid - 1
                #l = mid + 1
            else:
                l = mid + 1
                #r = mid - 1
        
        i, j = 0, len(matrix[0])-1
        print(r)

        while i <= j:
            mid = i + (j-i)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        return False
        
