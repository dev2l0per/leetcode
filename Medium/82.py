from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = None
        current = head
        next = current.next

        while next != None:
            if current.val == next.val:
                while next and current.val == next.val:
                    next = next.next
                if prev == None and next == None:
                    return None
                elif prev == None:
                    head = next
                    current = head
                    next = current.next
                else:
                    prev.next = next
                    current = prev
                    next = current.next
            else:
                prev = current
                current = current.next
                next = current.next
        return head