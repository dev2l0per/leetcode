class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        strMap = [0] * 26
        target = [0] * 26
        s1Length = len(s1)
        s2Length = len(s2)

        if s1Length > s2Length:
            return False

        for index in range(s1Length):
            strMap[ord(s1[index]) - 97] += 1
            strMap[ord(s2[index]) - 97] -= 1
        
        if strMap == target:
            return True
        
        for cur in range(s1Length, s2Length):
            strMap[ord(s2[cur - s1Length]) - 97] += 1
            strMap[ord(s2[cur]) - 97] -= 1

            if strMap == target:
                return True
        
        return False

sol = Solution()
print(sol.checkInclusion("ab", "a"))