# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # conceptually, to "remove" a node you just skip over it in the pointers
        # so that if node.val == val, just do curr.next.next
        thingy = ListNode(0)
        thingy.next = head
        curr = thingy

        while curr.next: # go until the list is traversed
            if curr.next.val == val: # if the next value is the target value to remove
                curr.next = curr.next.next # skip over it 
            else:
                curr = curr.next # else, just keep going 
 
        return thingy.next # lastly, return the list
        
