class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                val1 = nums[i] + nums[j]
                if val1 == target:
                    count += 1
                val2 = nums[j] + nums[i]
                if val2 == target:
                    count += 1
        return count
