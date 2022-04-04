class Solution:
    def decodeString(self, s: str) -> str:
        global idx
        idx = 0
        def dfs(s):
            result = ""
            global idx
            while idx < len(s) and s[idx] != ']':
                if not s[idx].isdigit():
                    result += s[idx]
                    idx += 1
                else:
                    iterN = 0
                    while idx < len(s) and s[idx].isdigit():
                        iterN = iterN * 10 + int(s[idx])
                        idx += 1
                    idx += 1
                    resDfs = dfs(s)
                    idx += 1
                    for _ in range(iterN):
                        result += resDfs
            return result
        
        return dfs(s)

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))