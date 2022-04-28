class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = list(s.split())
        length = len(slist[-1])
        return length
