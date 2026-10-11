# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tmp starts at index 1
        # prev and curr start at 0
        # move curr foward 

        if not head:
            return None

        curr = head
        prev = None
        tmp = curr.next

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev