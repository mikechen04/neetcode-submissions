# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def helper(root):
            nonlocal dia
            if not root:
                return 0
            else:
                leftDepth = helper(root.left)
                rightDepth = helper(root.right)
                if 1 + max(leftDepth, rightDepth) > dia:
                    dia = leftDepth + rightDepth
            return 1 + max(leftDepth, rightDepth)
        
        helper(root)
        return dia