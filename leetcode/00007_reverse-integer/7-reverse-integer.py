class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        digit = 0
        absX = abs(x)
        while absX:
            digit = absX % 10
            absX = absX // 10
            num = num * 10 + digit

        limit = 2**31 - 1
        if num > limit:
            return 0

        if x < 0:
            return num * -1
        else:
            return num
