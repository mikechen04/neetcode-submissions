class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # the premise here is to keep swapping duplicates within the list
        # until all the duplicates are at the end of the list

        # initialize l,r = 0,1
        # iterate through the loop
        # if left = right, r += 1
        # if left != right, left += 1, nums[left] = nums[right], r += 1
        # return l + 1

        l, r = 0, 1

        for i in range(len(nums) - 1):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1

        return l + 1