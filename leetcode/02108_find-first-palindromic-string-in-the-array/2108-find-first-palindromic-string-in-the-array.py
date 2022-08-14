class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            i = 0
            l = len(w)-1
            if i == l:
                return w
            flag = None

            while (i < l):
                if w[i] == w[l]:
                    flag = True
                    i += 1
                    l -= 1
                else:
                    flag = False
                    break
            if flag == True:
                return w
        return ""

        # for w in words:
        #     rev = w[::-1]
        #     if w == rev:
        #         return w
        # return ""
