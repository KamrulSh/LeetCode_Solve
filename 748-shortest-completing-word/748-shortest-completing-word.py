class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letter = []
        for i in licensePlate:
            if i.isalpha():
                letter.append(i.lower())
        table1 = Counter(letter)
        # print(table1)
        word_len = 1000
        memory = None
        for word in words:
            table2 = Counter(word)
            # print(table2)
            if table1 == table2:
                return word
            elif table1 < table2 and len(word) < word_len:
                word_len = len(word)
                memory = word
        return memory
    