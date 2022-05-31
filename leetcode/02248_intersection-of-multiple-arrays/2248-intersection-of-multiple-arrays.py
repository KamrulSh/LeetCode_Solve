class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ll = len(nums)
        dic = {}
        arr = []
        for i in range(ll):
            lla = len(nums[i])
            for j in range(lla):
                if nums[i][j] not in dic:
                    dic[nums[i][j]] = 1
                else:
                    dic[nums[i][j]] += 1

        for i in dic:
            if dic[i] == ll:
                arr.append(i)

        return sorted(arr)
