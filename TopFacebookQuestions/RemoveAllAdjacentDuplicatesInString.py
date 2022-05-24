from typing import Deque
from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: Deque = deque()

        for ch in s:
            if len(stack) == 0 or ch != stack[-1]:
                stack.append(ch)
            else:
                stack.pop()
        return ''.join(stack)