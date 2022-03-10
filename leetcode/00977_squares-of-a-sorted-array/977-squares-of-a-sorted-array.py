class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        newArr = [0] * len(nums)
        for idx in range(right, left-1, -1):
            if abs(nums[left]) < abs(nums[right]):
                newArr[idx] = nums[right] ** 2
                right -= 1
            else:
                newArr[idx] = nums[left] ** 2
                left += 1

        return newArr
