class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ss = ""
        count = 0
        for i in s:
            if i == "(":
                count += 1
                if count > 1:
                    ss += i
            else:
                count -= 1
                if count > 0:
                    ss += i

        return ss
