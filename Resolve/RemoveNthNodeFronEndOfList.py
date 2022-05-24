from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevNode: ListNode = None
        delNode: ListNode = head
        curNode: ListNode = head

        for _ in range(n):
            curNode = curNode.next
        while curNode:
            prevNode = delNode
            delNode = delNode.next
            curNode = curNode.next
        
        if delNode == head:
            return head.next
        prevNode.next = delNode.next
        return head