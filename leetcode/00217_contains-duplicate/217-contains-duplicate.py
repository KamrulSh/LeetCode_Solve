class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                return True

        return False
