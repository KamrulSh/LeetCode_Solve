class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for val in nums:
            if val != 0:
                nums[lastNonZero] = val
                lastNonZero += 1
        length = len(nums)
        for i in range(lastNonZero, length):
            nums[i] = 0

        # ----------- 2nd method
        # records the position of "0"
        # zero = 0
        # for i in xrange(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero += 1
