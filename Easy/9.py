class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverseNumber = 0
        number = x

        while x != 0:
            reverseNumber = reverseNumber * 10 + x % 10
            x = int(x / 10)
        print(reverseNumber)
        
        return number == reverseNumber

sol = Solution()
print(sol.isPalindrome(121))