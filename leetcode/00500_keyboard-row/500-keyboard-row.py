class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        arr = []
        for word in words:
            c1, c2, c3 = 0, 0, 0
            for w in word.lower():
                if w in l1:
                    c1 += 1
                elif w in l2:
                    c2 += 1
                else:
                    c3 += 1
            if len(word) == max(c1, c2, c3):
                arr.append(word)
        return arr
