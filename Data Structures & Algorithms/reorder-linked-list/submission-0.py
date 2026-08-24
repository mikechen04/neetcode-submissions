# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # split into head and part2 by using slow fast pointers to find the midpoint
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None

        # then, reverse part2
        prev = None
        curr = part2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge head and part2
        while head and prev:
            tmp = head.next
            tmp2 = prev.next
            head.next = prev
            if tmp:
                prev.next = tmp
            head = tmp
            prev = tmp2
    