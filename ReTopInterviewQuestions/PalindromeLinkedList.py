from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        traversal: List[int] = []

        cur: ListNode = head
        while cur:
            traversal.append(cur.val)
            cur = cur.next
        return traversal == traversal[::-1]
        
        # self.left: ListNode = head

        # def recursive(node: ListNode) -> bool:
        #     if node is None:
        #         return True
        #     if recursive(node.next) == False:
        #         return False
        #     if self.left.val != node.val:
        #         return False
        #     self.left = self.left.next
        #     return True
        # return recursive(head)