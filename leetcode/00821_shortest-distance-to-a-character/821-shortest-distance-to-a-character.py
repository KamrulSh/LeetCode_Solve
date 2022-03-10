class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occ = []
        dis = []
        for i in range(len(s)):
            if s[i] == c:
                occ.append(i)

        for i in range(len(s)):
            minVal = 9999999
            for j in range(len(occ)):
                val = abs(i-occ[j])
                if val < minVal:
                    minVal = val
            dis.append(minVal)

        return dis
