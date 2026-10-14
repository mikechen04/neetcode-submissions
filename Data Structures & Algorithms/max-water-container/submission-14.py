class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l, r = 0, len(heights)-1

        while l < r:
            res = (r - l) * min(heights[r], heights[l])
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            if res > maxi:
                maxi = res
        
        return maxi