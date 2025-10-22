"""
O(n)
sO(1)
merge here is bad, can be simplified breaking down cases
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
        temp = curr
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge
        normal = head
        reverse = prev
        while normal and reverse:
            normal_temp = normal.next
            normal.next = reverse
            reverse = reverse.next
            normal = normal.next

            if normal:
                normal.next = normal_temp
                normal = normal.next
