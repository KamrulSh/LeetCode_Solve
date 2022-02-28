class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num = ""
        for i in word:
            if i.isdigit():
                num += i
            else:
                num += " "
        num = num.split()
        num = set(map(int, num))
        return len(num)
