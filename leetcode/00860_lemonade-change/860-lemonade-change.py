class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
                if five == 0:
                    return False
                else:
                    five -= 1
            elif i == 20:
                if five == 0:
                    return False
                elif ten == 0 and five >= 3:
                    five -= 3
                elif ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                else:
                    return False
        return True
