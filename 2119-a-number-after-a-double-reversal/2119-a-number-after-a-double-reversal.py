class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        initial = num
        final = 0
        for i in range(2):
            rev_num = 0
            while num != 0:
                rem = num % 10
                rev_num = rev_num * 10 + rem
                num //= 10
            num = final = rev_num
        
        if initial == final:
            return True
        else:
            return False