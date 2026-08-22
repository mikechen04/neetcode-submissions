# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set() # to check which nodes were visited
        curr = head

        if head == None:
            return False
        
        while curr.next != None: # loop until a node does not exist anymore
            curr = curr.next
            visited.add(curr)
            if curr.next in visited: # cycle detected since its already been seen
                return True
            
        return False # loop exited, no cycle found