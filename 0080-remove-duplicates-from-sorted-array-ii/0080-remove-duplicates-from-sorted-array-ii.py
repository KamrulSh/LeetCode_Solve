class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 1
            if count <= 2:
                pos += 1
                nums[pos] = nums[i]
        return pos+1
