# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.findIsBalanced(root, 0, self.findDeepest(root))
        
    def findIsBalanced(self, root, depth, deepest):
        if not root:
            return True
        
        if root.left is None and root.right is None and deepest - depth > 1:
            return False

        left = self.findIsBalanced(root.left, depth + 1, deepest)
        right = self.findIsBalanced(root.right, depth + 1, deepest)

        if left and right:
            return True
        else:
            return False
    

    def findDeepest(self, root):
        if not root:
            return 0
        
        left = self.findDeepest(root.left)
        right = self.findDeepest(root.right)

        if left > right:
            return left + 1
        else:
            return right + 1
        