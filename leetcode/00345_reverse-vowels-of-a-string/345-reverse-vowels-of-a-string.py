class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = "aeiouAEIOU"
        s = list(s)

        # --------- method 1
        # vow = []
        # for i in range(len(s)):
        #     if s[i] in vowel:
        #         vow.append(i)

        # for i in range(len(vow)//2):
        #     s[vow[i]], s[vow[-1-i]] = s[vow[-1-i]], s[vow[i]]

        # --------- method 2
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] not in vowel:
                l += 1
            elif s[r] not in vowel:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        s = "".join(s)
        return s
