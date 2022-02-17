class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        table = {}
        for i in arr:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1

        count = 0
        for t in table:
            if table[t] == 1:
                count += 1
                if count == k:
                    return t
        return ""