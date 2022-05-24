from typing import Optional, Set

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet: Set = set()
        cur: ListNode = head

        while cur:
            if cur in hashSet:
                return cur
            hashSet.add(cur)
            cur = cur.next