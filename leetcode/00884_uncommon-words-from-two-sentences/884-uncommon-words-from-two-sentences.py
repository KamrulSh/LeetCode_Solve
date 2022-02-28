class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = Counter(s1.split() + s2.split())
        uncmn = []
        for word in table:
            if table[word] == 1:
                uncmn.append(word)

        # for word in table2:
        #     if table2[word] == 1 and word not in table1:
        #         uncmn.append(word)

        return uncmn
