"""
O(n)
sO(1)
forgor we dont need temp
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nextt = curr

        while curr is not None:
            nextt = nextt.next
            curr.next = prev
            prev = curr
            curr = nextt

        return prev
