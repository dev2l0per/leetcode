from typing import List, Dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash: Dict[int, int] = {}
        result: List[int] = []
        
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        sortList = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sortList[i][0])
        return result