class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break

        st = word[:idx+1][::-1]
        st += word[idx+1:]
        return st
