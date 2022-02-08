class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = 1001
        large = 0

        for num in nums:
            if num < small:
                small = num

            if num > large:
                large = num

        gcd = 1

        for i in range(1, small + 1):

            if (small % i == 0) and (large % i == 0):
                gcd = i

        return gcd