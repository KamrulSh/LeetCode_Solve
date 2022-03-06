class Solution:
    def freqAlphabets(self, s: str) -> str:
        alp = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        count = 0

        for i in range(len(s)-1, -1, -1):
            val = 0
            if s[i] == "#":
                val = int(s[i-2:i])
                count = 2
            else:
                if count > 0:
                    count -= 1
                    continue
                val = int(s[i])
            ans += alp[val-1]

        return ans[::-1]
