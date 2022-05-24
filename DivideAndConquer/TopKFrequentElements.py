from typing import List, Dict
from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict = Counter(nums)
        save: List[int] = list(count.keys())

        def partition(left: int, right: int, pivotIndex: int) -> int:
            pivotFrequency: int = count[save[pivotIndex]]
            save[pivotIndex], save[right] = save[right], save[pivotIndex]

            storeIndex: int = left
            for i in range(left, right):
                if count[save[i]] < pivotFrequency:
                    save[storeIndex], save[i] = save[i], save[storeIndex]
                    storeIndex += 1
            save[right], save[storeIndex] = save[storeIndex], save[right]
            return storeIndex
        def quickSelect(left: int, right: int, kSmallest: int) -> None:
            if left == right:
                return
            pivotIndex: int = random.randint(left, right)
            pivotIndex = partition(left, right, pivotIndex)
            if kSmallest == pivotIndex:
                return
            elif kSmallest < pivotIndex:
                quickSelect(left, pivotIndex - 1, kSmallest)
            else:
                quickSelect(pivotIndex + 1, right, kSmallest)
        n: int = len(save)
        quickSelect(0, n - 1, n - k)
        return save[n - k:]