class Solution:
    def minimumSum(self, num: int) -> int:
        ll = sorted(list(str(num)))
        n1 = ll[0] + ll[2]
        n2 = ll[1] + ll[3]
        sum = int(n1) + int(n2)
        return sum
