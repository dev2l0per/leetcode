from typing import Optional, List, Deque, Dict
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue: Deque = deque()
        hashTable: Dict = defaultdict(list)

        hashStart: int = 0
        hashEnd: int = 0

        queue.append((root, 0))

        result: List[List[int]] = []

        while queue:
            curNode: TreeNode
            verticalNum: int
            curNode, verticalNum = queue.popleft()

            hashTable[verticalNum].append(curNode.val)
            hashStart = min(hashStart, verticalNum)
            hashEnd = max(hashEnd, verticalNum)

            if curNode.left:
                queue.append((curNode.left, verticalNum - 1))
            if curNode.right:
                queue.append((curNode.right, verticalNum + 1))
        
        for i in range(hashStart, hashEnd + 1):
            result.append(hashTable[i])
        return result