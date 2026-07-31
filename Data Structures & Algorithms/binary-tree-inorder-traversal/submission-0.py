# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        self.traverse(root, solution)
        return solution

    def traverse(self, root, solution):
        if root is None:
            return None

        self.traverse(root.left, solution)
        solution.append(root.val)
        self.traverse(root.right, solution)

