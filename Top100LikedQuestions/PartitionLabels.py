from typing import List, Dict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash: Dict[str, int] = dict()
        result: List[int] = []

        for i, v in enumerate(s):
            hash[v] = i
        start: int = 0
        partMax: int = 0
        for i, v in enumerate(s):
            partMax = max(partMax, hash[v])
            if partMax == i:
                result.append(partMax - start + 1)
                start = partMax + 1
        return result