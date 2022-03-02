class Solution:
    def isHappy(self, n: int) -> bool:
        newset = set()
        while n != 1:
            sum = 0
            while n > 0:
                rem = n % 10
                sum += rem**2
                n //= 10

            if sum in newset:
                return False
            newset.add(sum)
            n = sum

        return True
