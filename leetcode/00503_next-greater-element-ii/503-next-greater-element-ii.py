class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # ------------ Approach 1 (Monotonic stack)
        stack = []
        nge = [-1] * len(nums)
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                popVal = stack.pop()
                nge[popVal] = num
            stack.append(idx)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                popVal = stack.pop()
                nge[popVal] = num

        return nge
