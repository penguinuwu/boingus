"""
O(n)
sO(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ret = ListNode(val=-math.inf, next=None)
        mainline = ret

        while list1 and list2:
            if list1.val <= list2.val:
                mainline.next = list1
                list1 = list1.next
            else:
                mainline.next = list2
                list2 = list2.next
            # increments mainline
            mainline = mainline.next

        # merge remainders
        mainline.next = list1 if list1 else list2

        return ret.next
