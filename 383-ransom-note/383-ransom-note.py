class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_stat = collections.Counter(ransomNote)
        magazine_stat = collections.Counter(magazine)
        return magazine_stat >= ransomNote_stat