class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ll = len(nums)
        curr_step = ll-1
        maxval = -1
        if nums[0] == 0 and ll > 1:
            return False
        for i in range(ll-1):
            if nums[i] >= curr_step:
                return True
            elif nums[i] == 0:
                for j in range(i):
                    if nums[j] > i-j:
                        break
                else:
                    return False
            curr_step -= 1
            maxval = nums[i]
            # print(nums[i], curr_step)
        return True