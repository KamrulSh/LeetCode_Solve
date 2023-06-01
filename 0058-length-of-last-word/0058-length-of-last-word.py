class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space, count = 0, 0
        for ch in s:
            count += 1
            if ch == " ":
                space = count
            else:
                length = count-space
        return length