# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None
        if n == 1:
            return lists[0]

        half = []
        while len(lists) >= 2:
            half.append(self.merge(lists.pop(), lists.pop()))
        half.extend(lists)

        return self.mergeKLists(half)


    def merge(self, a, b):
        head = None
        curr = None

        while a != None or b != None:
            tail = None

            if (b == None) or (a != None and a.val <= b.val):
                tail = a
                a = tail.next
            else:
                tail = b
                b = tail.next

            if head == None:
                head = tail
            else:
                curr.next = tail

            curr = tail

        return head
