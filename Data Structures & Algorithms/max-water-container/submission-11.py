class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights)-1

        while l < r:
            res = (r - l) * min(heights[l], heights[r])
            if heights[l] > heights[r]:
                r -= 1
                #res = min(l, r) ** 2
                # res = (r - l) * min(heights[l], heights[r])
            if res > maximum:
                maximum = res
            l += 1
        
        return maximum