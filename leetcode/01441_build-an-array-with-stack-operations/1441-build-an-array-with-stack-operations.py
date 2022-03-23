class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        # cnt = 0
        # for i in range(n+1):
        #     if cnt == len(target):
        #         return stack
        #     elif i+1 == target[cnt]:
        #         stack.append("Push")
        #         cnt += 1
        #     elif i+1 < target[cnt]:
        #         stack.append("Push")
        #         stack.append("Pop")

        # --------------- 2nd approach
        for i in range(1, target[-1]+1):
            stack.append("Push")
            if i not in target:
                stack.append("Pop")
        return stack
