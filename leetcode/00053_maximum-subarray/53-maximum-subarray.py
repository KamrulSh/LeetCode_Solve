class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_maxSum = -2**31
        current_max = 0
        for i in range(len(nums)):
            current_max += nums[i]
            if current_max > final_maxSum:
                final_maxSum = current_max

            if current_max < 0:
                current_max = 0
        return final_maxSum
