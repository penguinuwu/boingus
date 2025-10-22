"""
O(n)
sO(1)
loop can be refactored
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(val=-math.inf, next=None)
        mainline = ret

        while list1 or list2:
            if list1 is not None and (list2 is None or list1.val <= list2.val):
                mainline.next = list1
                mainline = mainline.next
                list1 = list1.next
            else:
                mainline.next = list2
                mainline = mainline.next
                list2 = list2.next
            mainline.next = None

        return ret.next
