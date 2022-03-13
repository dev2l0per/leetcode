class Solution:
    def reverseBits(self, n: int) -> int:
        result, mask = 0, 1

        for _ in range(32):
            result <<= 1
            result = result | n & mask
            n >>= 1
        return result

sol = Solution()
print(sol.reverseBits(43261596))