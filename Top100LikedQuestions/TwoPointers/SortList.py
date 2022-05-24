from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> ListNode:
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.val < head2.val:
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2

    def getMiddle(self, node: Optional[ListNode]) -> ListNode:
        slow: ListNode = node
        fast: ListNode = node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid: ListNode = self.getMiddle(head)
        midToNext: ListNode = mid.next
        mid.next = None

        return self.merge(self.sortList(head), self.sortList(midToNext))