class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for w in words:
            ll = len(w)
            if w == s[:ll]:
                count += 1
        return count
