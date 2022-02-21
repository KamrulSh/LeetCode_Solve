class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        # for i in range(len(nums)):
        #     if i % 10 == nums[i]:
        #         return i
        # return -1

        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1
