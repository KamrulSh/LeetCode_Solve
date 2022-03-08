class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = Counter(s)
        hash2 = Counter(t)
        if len(s) != len(t):
            return False

        for i in hash1:
            if i not in hash2 or hash1[i] != hash2[i]:
                return False
        return True
