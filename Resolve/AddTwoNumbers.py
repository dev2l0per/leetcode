from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry: bool = False

        cur1: ListNode = l1
        cur2: ListNode = l2

        dummy: ListNode = ListNode()
        curDummy: ListNode = dummy

        while cur1 or cur2:
            x: int = cur1.val if cur1 else 0
            y: int = cur2.val if cur2 else 0
            tempSum: int = x + y
            if carry is True:
                tempSum += 1
            carry = False
            if tempSum >= 10:
                tempSum -= 10
                carry = True
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            curDummy.next = ListNode(tempSum)
            curDummy = curDummy.next
        if carry:
            curDummy.next = ListNode(1)
        return dummy.next