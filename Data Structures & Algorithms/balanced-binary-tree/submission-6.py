# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            else:
                l = helper(root.left)
                r = helper(root.right)
                if l == -1 or r == -1:
                    return -1
                elif abs(l - r) > 1:
                    return -1
                else:
                    if l > r:
                        height = 1 + l
                    else:
                        height = 1 + r
            return height

        meow = helper(root)
        if meow == -1:
            return False
        else:
            return True