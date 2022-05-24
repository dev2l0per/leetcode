from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        result: ListNode = None
        if left is None:
            return right
        if right is None:
            return left
        if left.val <= right.val:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def getMiddle(slef, node: ListNode) -> ListNode:
        if node is None:
            return node

        slow: ListNode = node
        fast: ListNode = node

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        mid: ListNode = self.getMiddle(head)
        nextToMid: ListNode = mid.next

        mid.next = None
        left: ListNode = self.sortList(head)
        right: ListNode = self.sortList(nextToMid)
        return self.merge(left, right)