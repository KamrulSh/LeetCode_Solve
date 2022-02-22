class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        sum = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

        for sym in s[::-1]:
            if prev > roman[sym]:
                sum -= roman[sym]
            else:
                sum += roman[sym]
            prev = roman[sym]
        return sum
