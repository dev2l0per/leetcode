from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode(0, head)
        prevNode: ListNode = dummy
        curNode: ListNode = head

        while curNode:
            if curNode.next and curNode.val == curNode.next.val:
                while curNode.next and curNode.val == curNode.next.val:
                    curNode = curNode.next
                prevNode.next = curNode.next
            else:
                prevNode = prevNode.next
            curNode = curNode.next
        return dummy.next