# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        endNode = dummyNode
        while True:
            if l1 is None:
                endNode.next = l2
                break
            if l2 is None:
                endNode.next = l1
                break

            if l1.val <= l2.val:
                endNode.next = l1
                l1 = l1.next
            else:
                endNode.next = l2
                l2 = l2.next
            endNode = endNode.next

        return dummyNode.next
