"""
O(n)
sO(n)
check solution
can use range-index because inorder is ALWAYS continuous
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal curr_preorder_index

            if left == right:
                return None

            curr_root_value = preorder[curr_preorder_index]
            curr_preorder_index += 1

            root_inorder_index = inorder_index[curr_root_value]
            left_node = helper(left, root_inorder_index)
            right_node = helper(root_inorder_index + 1, right)

            return TreeNode(val=curr_root_value, left=left_node, right=right_node)

        inorder_index = {v: i for i, v in enumerate(inorder)}
        curr_preorder_index = 0
        return helper(0, len(preorder))
