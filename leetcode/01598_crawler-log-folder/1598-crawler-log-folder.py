class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #         folder = []
        #         for i in logs:
        #             if i == "../":
        #                 if len(folder) > 0:
        #                     folder.pop()
        #             elif i == "./":
        #                 continue
        #             else:
        #                 folder.append(i)

        #         return len(folder)

        step = 0
        for op in logs:
            if op == "../":
                step -= 1
            elif op == "./":
                continue
            else:
                step += 1
            step = max(step, 0)
        return step
