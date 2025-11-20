"""
O(n)
sO(n)
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
            if node is None:
                return 0, 0

            left_max_d, left_max = helper(node.left)
            right_max_d, right_max = helper(node.right)
            return (
                max(left_max_d, right_max_d) + 1,
                max(left_max_d + right_max_d, left_max, right_max),
            )

        return helper(root)[1]
