class Solution:
    def toLowerCase(self, s: str) -> str:
        low = ""
        for i in s:
            val = ord(i)
            if val >= 65 and val <= 90:
                low += chr(val + 32)
            else:
                low += i
        return low
