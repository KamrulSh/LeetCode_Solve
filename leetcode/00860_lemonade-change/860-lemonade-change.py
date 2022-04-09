class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        table = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                table[5] += 1
            elif i == 10:
                table[10] += 1
                if table[5] == 0:
                    return False
                else:
                    table[5] -= 1
            elif i == 20:
                if table[5] == 0:
                    return False
                elif table[10] == 0 and table[5] >= 3:
                    table[5] -= 3
                elif table[10] > 0 and table[5] > 0:
                    table[5] -= 1
                    table[10] -= 1
                else:
                    return False
        return True
