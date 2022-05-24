from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash: Dict[str, List[str]] = {}

        for str in strs:
            sortStr = ''.join(sorted(str))
            if sortStr not in hash:
                hash[sortStr] = []
            hash[sortStr].append(str)
        return hash.values()