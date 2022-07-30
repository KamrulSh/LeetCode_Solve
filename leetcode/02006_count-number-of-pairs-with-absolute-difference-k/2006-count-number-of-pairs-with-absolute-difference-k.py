class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        len_list = len(nums)
        for i in range(len_list-1):
            for j in range(i + 1, len_list):
                if abs(nums[i]-nums[j]) == k:
                    count += 1
        return count
