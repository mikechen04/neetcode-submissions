class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_temp = []

        for i in range(m):
            nums1_temp.append(nums1[i])
        
        nums1.clear()
        #nums1_temp == nums1
        
        for i in range(m):
            nums1.append(nums1_temp[i])

        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()
        # nums1_temp == nums1
        # nums1.clear()