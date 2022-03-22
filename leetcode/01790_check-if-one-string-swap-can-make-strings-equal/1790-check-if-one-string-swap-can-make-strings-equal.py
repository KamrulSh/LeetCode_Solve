class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        table = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                table.append((s1[i], s2[i]))
        # print(table)
        if len(table) == 0:
            return True
        elif len(table) == 2:
            if table[0][0] == table[1][1] and table[0][1] == table[1][0]:
                return True
        else:
            return False
