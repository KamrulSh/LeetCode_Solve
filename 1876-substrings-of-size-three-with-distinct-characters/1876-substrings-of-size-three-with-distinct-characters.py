class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(s) < 3:
            return count
        for i in range(len(s)-2):
            subStr = s[i:i+3]
            if subStr[0] != subStr[1] and subStr[0] != subStr[2] and subStr[1] != subStr[2]:
                count += 1
        return count