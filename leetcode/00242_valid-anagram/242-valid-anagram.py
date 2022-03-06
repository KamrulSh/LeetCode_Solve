class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1

        for i in t:
            if i not in hash2:
                hash2[i] = 1
            else:
                hash2[i] += 1

        for i in hash1:
            if i not in hash2 or hash1[i] != hash2[i]:
                return False
        return True
