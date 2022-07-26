class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter = []
        ll = len(s)
        for i in range(ll):
            if s[i] not in letter:
                letter.append(s[i])
            else:
                return s[i]
