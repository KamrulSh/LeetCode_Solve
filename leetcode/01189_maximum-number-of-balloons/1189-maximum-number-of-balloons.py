class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balon"
        table = {}
        for i in text:
            if i in word:
                if i not in table:
                    table[i] = 1
                else:
                    table[i] += 1

        if len(table) == 5:
            table['l'] //= 2
            table['o'] //= 2
            minVal = min(table.values())
        else:
            minVal = 0
        return minVal
