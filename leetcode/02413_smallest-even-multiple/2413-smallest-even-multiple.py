class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            ans = 2 * n
        else:
            ans = n
        return ans
