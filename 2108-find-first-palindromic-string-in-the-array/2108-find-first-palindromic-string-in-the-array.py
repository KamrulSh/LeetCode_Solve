class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            rev = w[::-1]
            if w == rev:
                return w
        return ""