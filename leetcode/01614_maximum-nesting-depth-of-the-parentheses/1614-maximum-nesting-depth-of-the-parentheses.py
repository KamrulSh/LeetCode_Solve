class Solution:
    def maxDepth(self, s: str) -> int:
        maxval = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                maxval = max(maxval, count)
                count -= 1

        return maxval
