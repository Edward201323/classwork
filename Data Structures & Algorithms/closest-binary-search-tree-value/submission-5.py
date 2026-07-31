# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        closest_difference = abs(target - closest)

        def dfs(curr):
            if not curr:
                return
            nonlocal closest, closest_difference

            curr_difference = abs(target - curr.val)
            if curr_difference < closest_difference:
                closest_difference = curr_difference
                closest = curr.val
            
            if target <= curr.val:
                dfs(curr.left)
            else:
                dfs(curr.right)

        dfs(root)
        return closest