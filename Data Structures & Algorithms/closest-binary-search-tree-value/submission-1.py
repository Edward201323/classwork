# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    closest = -1
    closest_difference = -1
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1
        self.closest = root.val
        self.closest_difference = abs(target - root.val)
        self.getClosestValue(root, target)
        return self.closest


    def getClosestValue(self, root, target):
        if not root:
            return

        difference = abs(target - root.val)
        if difference < self.closest_difference:
            self.closest = root.val
            self.closest_difference = difference

        if target < root.val:
            self.getClosestValue(root.left, target)
        else:
            self.getClosestValue(root.right, target)