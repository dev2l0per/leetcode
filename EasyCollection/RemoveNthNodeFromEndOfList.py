from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, delNode, cur = None, head, head

        for _ in range(n):
            cur = cur.next
        
        while cur:
            prev = delNode
            delNode = delNode.next
            cur = cur.next
        
        if delNode == head:
            return head.next

        prev.next = delNode.next
        return head