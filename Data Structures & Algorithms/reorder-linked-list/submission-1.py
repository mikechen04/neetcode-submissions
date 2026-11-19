# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        slow = head
        fast = head
        while fast and fast.next: # grab the midpoint
            slow = slow.next
            fast = fast.next.next
        
        curr = slow # midpoint aka l2 (l1 is head, l2 start is slow)
        nxt = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is now the start of reversed l2
        l2 = prev

        # then, alternate between l1 and l2 and put them together
        dummy = node = ListNode()
        while l1.next and l2.next:
            node.next = l1
            l1 = l1.next
            node = node.next
            node.next = l2
            l2 = l2.next
            node = node.next
        
        node.next = l1 or l2


