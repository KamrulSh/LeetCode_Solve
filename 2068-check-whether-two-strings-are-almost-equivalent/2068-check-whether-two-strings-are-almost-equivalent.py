class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
#         table1 = {}
#         table2 = {}
#         for i in word1:
#             if i not in table1:
#                 table1[i] = 1
#             else:
#                 table1[i] += 1
        
#         for i in word2:
#             if i not in table2:
#                 table2[i] = 1
#             else:
#                 table2[i] += 1
        
        
        table1 = Counter(word1)
        table2 = Counter(word2)
        for item in table2:
            if item not in table1:
                table1[item] = table2[item]
            else:
                table1[item] = abs(table1[item]-table2[item])
        
        for i in table1:
            if table1[i] > 3:
                return False
        return True