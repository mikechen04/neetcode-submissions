class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxvolume = min(heights[l], heights[r]) * (r-l)

        while l <= r:
            volume = min(heights[l], heights[r]) * (r-l)
            if volume > maxvolume:
                maxvolume = volume
                
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            

        return maxvolume # length * width