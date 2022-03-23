class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                popVal = stack.pop()
                # concept of next greater element
                # find the diff of NGE position and pop value
                answer[popVal] = idx - popVal
            stack.append(idx)
        # print(answer)
        return answer
