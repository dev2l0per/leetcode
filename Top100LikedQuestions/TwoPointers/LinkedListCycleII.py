from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        fast: ListNode = head
        slow: ListNode = head

        while True:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        ptr1: ListNode = head
        ptr2: ListNode = fast
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1