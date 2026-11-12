class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m, n
        while l <= (m+n-1):
            nums1[l] = nums2[r-2]
            l += 1
            r += 1
        nums1.sort()
        
        