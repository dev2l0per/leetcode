from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        result = None
        if list1.val <= list2.val:
            result = ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            result = ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return result

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
print(sol.mergeTwoLists(list1, list2))