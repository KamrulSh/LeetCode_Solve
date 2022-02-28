class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_tbl = Counter(s)
        t_tbl = Counter(t)
        count = 0
        # string s
        for i in t_tbl:
            if i not in s_tbl:
                count += t_tbl[i]
            elif t_tbl[i] > s_tbl[i]:
                count += t_tbl[i]-s_tbl[i]

        # string t
        for i in s_tbl:
            if i not in t_tbl:
                count += s_tbl[i]
            elif s_tbl[i] > t_tbl[i]:
                count += s_tbl[i]-t_tbl[i]

        return count
