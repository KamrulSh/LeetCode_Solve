class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            total = 0
            while i != 0:
                rem = i % 10
                i //= 10
                total += rem
            if total % 2 == 0:
                count += 1
                
        return count