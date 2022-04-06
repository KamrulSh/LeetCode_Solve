class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c1 = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        for i in range(len(t)):
            if t[i] == s[c1]:
                c1 += 1
            if c1 == len(s):
                return True
        else:
            return False
