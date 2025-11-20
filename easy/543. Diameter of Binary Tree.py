"""
O(n)
sO(n)
check solution
use global result instead of return
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal diameter

            if node is None:
                return 0

            left_depth = helper(node.left)
            right_depth = helper(node.right)

            diameter = max(left_depth + right_depth, diameter)
            return max(left_depth, right_depth) + 1

        diameter = 0
        helper(root)
        return diameter
