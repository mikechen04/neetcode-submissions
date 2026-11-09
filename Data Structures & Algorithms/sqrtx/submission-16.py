class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        if x == 0:
            return 0

        while l <= r:
            mid = l + ((r-l)//2)
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid + 1
            elif mid*mid > x:
                r = mid - 1
        
        return math.floor(l-1)