class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        pos = 0
        for sen in sentence:
            ls = len(sen)
            lsw = len(searchWord)
            pos += 1
            if ls >= lsw and sen[:lsw] == searchWord:
                return pos
        return -1
