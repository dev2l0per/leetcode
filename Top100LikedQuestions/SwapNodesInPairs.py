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

        cur: ListNode = head
        newCur: ListNode = newList

        while cur and cur.next:
            curNode: ListNode = cur
            nextNode: ListNode = cur.next

            newCur.next = nextNode
            curNode.next = nextNode.next
            nextNode.next = curNode

            newCur = curNode
            cur = curNode.next
        return newList.next