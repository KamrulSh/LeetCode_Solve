class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for key, value in enumerate(nums):
            lookup = target-value
            if lookup in hashMap:
                return [hashMap[lookup], key]
            else:
                hashMap[value] = key
