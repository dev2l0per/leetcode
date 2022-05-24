from typing import Optional, Deque
from collections import deque

# Definition for a Node
class Node:
    def __init__(self, val: int=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        
        queue: Deque = deque()
        queue.append(root)

        while queue:
            curLen: int = len(queue)
            while curLen > 0:
                cur: Node = queue.popleft()
                if curLen > 1:
                    cur.next = queue[0]
                curLen -= 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root