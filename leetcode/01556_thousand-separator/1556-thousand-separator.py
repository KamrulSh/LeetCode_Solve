class Solution:
    def thousandSeparator(self, n: int) -> str:
        newStr = ""
        count = 0
        n = str(n)
        for i in range(len(n)-1, -1, -1):
            if count == 3:
                newStr = "." + newStr
                count = 0
            newStr = n[i] + newStr
            count += 1
        return newStr
