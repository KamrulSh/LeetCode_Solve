class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # ------------- method 1

        # table = {}
        # values = []
        # if n == 1:
        #     return n

        # for a,b in trust:
        #     if b not in table:
        #         table[b] = 1
        #     else:
        #         table[b] += 1
        #     values.append(a)

        # for i in table:
        #     if table[i] == n-1:
        #         if i not in values:
        #             return i
        # return -1

        # ------------- method 2
        count = [0]*(n+1)

        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        for i in range(1, n+1):
            if count[i] == n-1:
                return i

        return -1
