class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pop1 = len(nums1) - m
        pop2 = len(nums2) - n

        for i in range(pop1):
            nums1.pop()
        
        for j in range(pop2):
            nums2.pop()

        nums1 += nums2
        nums1.sort()
