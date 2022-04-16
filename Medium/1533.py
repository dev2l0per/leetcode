# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#     # Compares the sum of arr[l..r] with the sum of arr[x..y]
#     # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#     # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#     # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#     def compareSub(self, l: int, r: int, x: int, y: int) -> int:
    
#     # Returns the length of the array
#     def length(self) -> int:
# 

import math

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        length = reader.length()
        l, x = 0, length // 2
        
        while l <= x:
            length = math.ceil(length / 2)
            val = reader.compareSub(l, l + length - 1, x, x + length - 1)

            if val == 1:
                x = l + (length // 2)
            elif val == -1:
                l = x
                x = x + (length // 2)
            else:
                return l + length - 1
        return l