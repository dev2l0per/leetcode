from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(nums[mid], create(l, mid - 1), create(mid + 1, r))
        return create(0, len(nums) - 1)