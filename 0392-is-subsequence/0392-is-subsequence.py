class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for i in range(len(s)):
            ent = 0
            for j in range(pos, len(t)):
                if s[i] == t[j]:
                    pos = j+1
                    ent = 1
                    break
            if ent == 0:
                return False
        return True