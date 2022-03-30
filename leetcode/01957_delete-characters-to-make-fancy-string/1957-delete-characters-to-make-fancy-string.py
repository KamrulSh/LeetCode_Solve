class Solution:
    def makeFancyString(self, s: str) -> str:
        newStr = ""
        ll = len(s)
        if ll < 3:
            return s
        for i in range(ll-2):
            if i == 0 and s[i] == s[i+1] and s[i+1] == s[i+2]:
                newStr += s[i] + s[i+1]
            elif i == 0:
                newStr += s[i] + s[i+1] + s[i+2]
            elif s[i] == s[i+1] and s[i+1] == s[i+2]:
                continue
            else:
                newStr += s[i+2]
        return newStr
