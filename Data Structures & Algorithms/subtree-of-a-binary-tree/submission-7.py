# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            
        def helper(node):
            if not node:
                return False
            
            return sameTree(node, subRoot) or helper(node.left) or helper(node.right)
            
        return helper(root)
            