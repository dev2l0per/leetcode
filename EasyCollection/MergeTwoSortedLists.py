from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        cur1, cur2, newCur = list1, list2, newHead

        while True:
            if cur1 is None and cur2 is None:
                break
            if cur1 is None:
                newCur.next = cur2
                cur2 = cur2.next
                newCur = newCur.next
            elif cur2 is None:
                newCur.next = cur1
                cur1 = cur1.next
                newCur = newCur.next
            else:
                if cur1.val > cur2.val:
                    newCur.next = cur2
                    cur2 = cur2.next
                else:
                    newCur.next = cur1
                    cur1 = cur1.next
                newCur = newCur.next
        return newHead.next