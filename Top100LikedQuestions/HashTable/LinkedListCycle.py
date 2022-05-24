from typing import Optional, Set

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet: Set[ListNode] = set()
        cur: ListNode = head

        while cur:
            if cur in hashSet:
                return True
            hashSet.add(cur)
            cur = cur.next
        return False