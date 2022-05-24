from typing import List, Dict
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap: Dict = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(s))
            hashMap[sortedStr].append(s)
        return hashMap.values()