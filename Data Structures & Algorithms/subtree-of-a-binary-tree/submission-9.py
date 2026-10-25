# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root and subRoot:
                return False
            elif not subRoot and root:
                return False

            if root.val == subRoot.val:
                if isSame(root.left, subRoot.left) is True and isSame(root.right, subRoot.right) is True:
                    return True
            
            return False

        def helper(root, subRoot):
            if root is None:
                return False

            if isSame(root, subRoot) is True:
                return True
            elif helper(root.left, subRoot) is True or helper(root.right, subRoot) is True:
                return True
            
            return False

        return helper(root, subRoot)