from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])

        if not root:
            return root
        while queue:
            curQueueSize = len(queue)
            for index in range(curQueueSize):
                curNode = queue.popleft()

                if index < curQueueSize - 1:
                    curNode.next = queue[0]
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
        return root