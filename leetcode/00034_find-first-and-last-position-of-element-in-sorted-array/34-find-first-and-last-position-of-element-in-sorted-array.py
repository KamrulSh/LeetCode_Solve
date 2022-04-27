class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        leftP = self.binarySearchLeft(nums, target)
        rightP = self.binarySearchRight(nums, target)

        return [leftP, rightP] if leftP <= rightP else [-1, -1]

    def binarySearchLeft(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def binarySearchRight(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right
