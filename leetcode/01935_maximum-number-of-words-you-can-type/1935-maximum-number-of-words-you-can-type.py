class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = 0
        for word in text:
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                count += 1
        return count
