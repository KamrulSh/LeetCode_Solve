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
                if curBracket == "(":
                    if bracket != ")":
                        return False
                if curBracket == "{":
                    if bracket != "}":
                        return False
                if curBracket == "[":
                    if bracket != "]":
                        return False
        if stack:
            return False
        else:
            return True
