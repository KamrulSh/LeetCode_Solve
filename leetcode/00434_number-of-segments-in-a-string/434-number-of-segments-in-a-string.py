class Solution:
    def countSegments(self, s: str) -> int:
        # s = s.split()
        # return len(s)

        # ------------ Approach 3
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count

        # ------------ Approach 2
        '''
        count = 0
        ite = iter(s)
        while True:
            try:
                while next(ite) == " ":
                    continue
                else:
                    count += 1
                while next(ite) != " ":
                    continue
            except StopIteration:
                return count
        '''
