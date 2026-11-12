class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 1: # base case
            return False

        # we can use a set to figure out if there is a duplicate
        # if not, we can increment foward and remove the first element put into the set
        # return True if we go to the end of the array with no duplicates

        seen = set(nums[0:k-1])
        for r in range(0, len(nums)-1):
            seen.add(nums[r])
            if nums[r] in seen:
                return True
            else:
                seen.remove(nums[r])

        print(seen)
        return False
