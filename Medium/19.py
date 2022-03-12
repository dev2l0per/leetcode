from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        delNode = curNode = head

        for _ in range(n - 1):
            if curNode.next == None:
                return None
            curNode = curNode.next
        
        while curNode.next != None:
            delNode = delNode.next
            curNode = curNode.next

        if delNode.next != None:
            delNode.next = delNode.next.next

        return head
