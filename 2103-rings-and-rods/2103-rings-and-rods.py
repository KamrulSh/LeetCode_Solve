class Solution:
    def countPoints(self, rings: str) -> int:
        table = {}
        for i in range(1, len(rings), 2):
            if rings[i] not in table:
                table[rings[i]] = list(rings[i-1])
            else:
                if rings[i-1] not in table[rings[i]]:
                    table[rings[i]].append(rings[i-1])
        # print(table)
        
        count = 0
        for i in table:
            if len(table[i]) == 3:
                count += 1
        return count