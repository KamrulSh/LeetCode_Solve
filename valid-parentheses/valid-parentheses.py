class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                curBracket = stack.pop()
                if curBracket == "(" and bracket != ")":
                    return False
                elif curBracket == "{" and bracket != "}":
                    return False
                elif curBracket == "[" and bracket != "]":
                    return False
        if stack:
            return False
        else:
            return True