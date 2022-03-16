from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                cur: Node = queue.popleft()
                
                if i < queueLength - 1:
                    cur.next = queue[0]

                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
        
        return root