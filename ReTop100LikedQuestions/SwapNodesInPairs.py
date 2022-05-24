from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList: ListNode = ListNode()
        newList.next = head

        curNode: ListNode = head
        newCurNode: ListNode = newList

        while curNode and curNode.next:
            cur: ListNode = curNode
            next: ListNode = curNode.next

            newCurNode.next = next
            cur.next = next.next
            next.next = cur

            newCurNode = cur
            curNode = cur.next
        return newList.next