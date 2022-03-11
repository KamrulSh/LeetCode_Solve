# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        demoNode = ListNode(-1)
        demoNode.next = head
        currentNode = demoNode
        while currentNode.next:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return demoNode.next
