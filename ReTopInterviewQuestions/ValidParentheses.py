from typing import Deque
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack: Deque = deque()
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                cur: str = stack.pop()
                if cur == '(' and ch != ')':
                    return False
                if cur == '[' and ch != ']':
                    return False
                if cur == '{' and ch != '}':
                    return False
        if len(stack) != 0:
            return False
        return True