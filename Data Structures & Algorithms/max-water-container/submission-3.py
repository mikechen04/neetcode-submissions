class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights)-1

        for i in range(len(heights)-1):
            if heights[l] >= heights[l+1] and heights[r] >= heights[r-1]:
                #res = min(l, r) ** 2
                res = (r - i) * min(heights[l], heights[r])
                if res > maximum:
                    maximum = res
                    l += 1
                    r -= 1
            elif heights[l+1] > heights[l]:
                l += 1
            elif heights[r-1] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maximum