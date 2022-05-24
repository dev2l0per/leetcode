from typing import Optional

# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node: ListNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node