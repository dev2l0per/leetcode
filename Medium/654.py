from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(numList: List[int], start, end):
            if start >= end:
                return None
            maxNum = max(numList)
            maxIndex = numList.index(maxNum)
            root = TreeNode(maxNum)
            root.left = construct(numList[start:maxIndex], start, maxIndex)
            root.right = construct(numList[maxIndex + 1:end], 0, len(numList[maxIndex + 1:end]))
            
            return root
        return construct(nums, 0, len(nums))