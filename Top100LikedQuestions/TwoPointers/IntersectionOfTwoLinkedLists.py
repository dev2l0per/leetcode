from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA: ListNode = headA
        curB: ListNode = headB

        while curA != curB:
            if curA is None:
                curA = headB
                continue
            if curB is None:
                curB = headA
                continue
            curA = curA.next
            curB = curB.next
        return curA