class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        table = collections.Counter(nums)
        # for key, val in table.items():
        #     if val % 2 != 0:
        #         return False
        # return True

        # approach 2 -------> one line
        return all(val % 2 == 0 for val in table.values())
