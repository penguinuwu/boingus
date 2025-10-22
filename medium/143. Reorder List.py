"""
O(n)
sO(1)
merge is done by saving 2 temps
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find midpoint
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        midpoint = slow.next
        slow.next = None

        # reverse 2nd half
        prev = None
        curr = midpoint
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge
        normal = head
        reverse = prev
        while reverse:
            normal_next = normal.next
            reverse_next = reverse.next

            normal.next = reverse
            reverse.next = normal_next

            normal = normal_next
            reverse = reverse_next
