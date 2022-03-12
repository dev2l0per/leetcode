from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        cur = result
        carry = 0
        while True:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            cur.next = ListNode((x + y + carry) % 10)
            cur = cur.next
            carry = int((x + y + carry) / 10)
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
            if l1 == None and l2 == None:
                if carry != 0:
                    cur.next = ListNode(carry)
                break
        return result.next

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
while result != None:
    print(result.val)
    result = result.next