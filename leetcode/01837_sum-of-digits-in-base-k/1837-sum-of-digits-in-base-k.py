class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n != 0:
            rem = n % k
            n = n // k
            total += rem
        return total
