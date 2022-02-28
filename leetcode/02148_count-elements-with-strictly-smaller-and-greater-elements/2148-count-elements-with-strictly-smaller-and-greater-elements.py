class Solution:
    def countElements(self, nums: List[int]) -> int:
        minVal = min(nums)
        maxVal = max(nums)
        table = Counter(nums)
        nums.sort()
        ll = len(nums)
        diff = ll - table[minVal] - table[maxVal]
        if ll < 3 or diff < 0:
            return 0
        else:
            return diff
