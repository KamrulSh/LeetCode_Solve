class Solution:
    def minimumSum(self, num: int) -> int:
        # ll = sorted(list(str(num)))
        # n1 = ll[0] + ll[2]
        # n2 = ll[1] + ll[3]
        # sum = int(n1) + int(n2)
        # return sum

        digits = []
        while num != 0:
            rem = num % 10
            digits.append(rem)
            num = num // 10

        digits.sort()
        min_total = 10*(digits[0] + digits[1]) + digits[2]+digits[3]
        return min_total
