# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.helper(root)

        return self.max_diameter
        
    def helper(self, root: Optional[TreeNode]):
        if not root:
            return 0

        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)

        self.max_diameter = max(self.max_diameter, leftDepth + rightDepth)

        return 1 + max(leftDepth, rightDepth)
        