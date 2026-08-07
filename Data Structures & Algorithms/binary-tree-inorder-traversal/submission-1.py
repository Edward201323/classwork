# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        self.traverse(root, sol)
        return sol

    def traverse(self, root, sol):
        if not root:
            return
            
        self.traverse(root.left, sol)
        sol.append(root.val)
        self.traverse(root.right, sol)