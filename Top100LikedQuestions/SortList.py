from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(head1: Optional[ListNode], head2: Optional[ListNode]) -> ListNode:
    if head1 and head2:
        if head1.val > head2.val:
            head1, head2 = head2, head1
        head1.next = merge(head1.next, head2)
    return head1 or head2

    # dummy: ListNode = ListNode()
    # cur: ListNode = dummy

    # while head1 or head2:
    #     if head1 is None and head2 is None:
    #         break
    #     if head1 is None:
    #         cur.next = ListNode(head2.val)
    #         cur = cur.next
    #         head2 = head2.next
    #     elif head2 is None:
    #         cur.next = ListNode(head1.val)
    #         cur = cur.next
    #         head1 = head1.next
    #     else:
    #         if head1.val >= head2.val:
    #             cur.next = ListNode(head2.val)
    #             head2 = head2.next
    #         else:
    #             cur.next = ListNode(head1.val)
    #             head1 = head1.next
    #         cur = cur.next

    # return dummy.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid: ListNode = None
        slow: ListNode = head
        fast: ListNode = head

        while fast and fast.next:
            mid, slow, fast = slow, slow.next, fast.next.next

        mid.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return merge(left, right)