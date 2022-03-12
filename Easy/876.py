from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index1 = index2 = head

        while index2 and index2.next:
            index1 = index1.next
            index2 = index2.next.next
        return index1

sol = Solution()
print(sol.middleNode([1, 2, 3, 4, 5]))