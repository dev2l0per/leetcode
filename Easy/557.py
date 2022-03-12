class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split(" ")
        result = ""

        for idx in range(len(wordList)):
            wordList[idx] = wordList[idx][::-1]
        result = " ".join(wordList)
        
        return result

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))