class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i.lstrip("-").isnumeric():
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                val = 2 * stack[-1]
                stack.append(val)
            elif i == "+":
                val = stack[-2] + stack[-1]
                stack.append(val)
            # if statement can be done with else
            # else:
            #     stack.append(int(i))
            # print(stack)
        return sum(stack)
