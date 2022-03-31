class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        table = dict()
        for word in words:
            for i in word:
                table[i] = table.get(i, 0) + 1
        ll = len(words)
        for item in table:
            if table[item] % ll != 0:
                return False
        return True
