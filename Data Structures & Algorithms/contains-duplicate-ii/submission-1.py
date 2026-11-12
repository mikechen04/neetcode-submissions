class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = 0
        res = 0
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = num

        for r in range(len(nums)):
            window += nums[r]
            while window > k:
                if num in seen and r - seen[num] <= k:
                    return True
                window -= nums[l]
                l += 1
        
        return False