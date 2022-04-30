from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseList(self, head: Optional[TreeNode]) -> Optional[TreeNode]:
        prev: Optional[TreeNode] = None
        cur: Optional[TreeNode] = head

        while cur:
            tempNext: Optional[TreeNode] = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev