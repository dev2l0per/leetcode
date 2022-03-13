class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sCur, tCur = len(s) - 1, len(t) - 1
        sBackCount, tBackCount = 0, 0

        while True:
            if s[sCur] == '#' and sCur >= 0:
                sCur -= 1
                sBackCount += 1
                continue
            elif t[tCur] == '#' and tCur >= 0:
                tCur -= 1
                tBackCount += 1
                continue

            if sBackCount > 0:
                sCur -= 1
                sBackCount -= 1
                continue
            elif tBackCount > 0:
                tCur -= 1
                tBackCount -= 1
                continue

            if sCur == -1 or tCur == -1:
                break

            if s[sCur] != t[tCur]:
                break
            sCur -= 1
            tCur -= 1

        if sCur <= -1 and tCur <= -1:
            return True
        return False

sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))
print(sol.backspaceCompare("a#c", "b"))
print(sol.backspaceCompare("bxj##tw", "bxo#j##tw"))
print(sol.backspaceCompare("bxj##tw", "bxj###tw"))
print(sol.backspaceCompare("ab##", "c#d#"))
print(sol.backspaceCompare("a##c", "#a#c"))
print(sol.backspaceCompare("aaa###a", "aaaa###a"))