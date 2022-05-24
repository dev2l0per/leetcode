from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        maxNum: int = max(nums)
        maxIndex: int = nums.index(maxNum)
        return TreeNode(maxNum, self.constructMaximumBinaryTree(nums[:maxIndex]), self.constructMaximumBinaryTree(nums[maxIndex + 1:]))