class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights)-1

        while l < r:
            if heights[l] == heights[r]:
                #res = min(l, r) ** 2
                res = (r - l) * min(heights[l], heights[r])
                if res > maximum:
                    maximum = res
                l += 1
                r -= 1
            elif heights[l+1] > heights[l]:
                r -= 1
            elif heights[r-1] > heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        
        return maximum