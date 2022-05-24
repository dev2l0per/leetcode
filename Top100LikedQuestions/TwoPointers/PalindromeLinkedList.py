from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left: ListNode = head

        def recursive(node: Optional[ListNode]) -> bool:
            if node:
                if recursive(node.next) == False:
                    return False
                if self.left.val != node.val:
                    return False
                self.left = self.left.next
            return True
        return recursive(head)
        
        # lst: List[int] = []
        # cur: ListNode = head

        # while cur:
        #     lst.append(cur.val)
        #     cur = cur.next
        # return lst == lst[::-1]